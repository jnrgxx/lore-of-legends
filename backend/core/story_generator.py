from sqlalchemy.orm import Session
from core.config import settings

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser # take a str response from LLM > pipe it into python Class

from core.prompts import STORY_PROMPT
from models.story import Story, StoryNode
from core.models import StoryLLMResponse, StoryNodeLLM

class StoryGenerator:

    @classmethod
    def _get_llm(cls): # underscore @ start bcoz it's Private Method
        #return ChatOpenAI(model="gpt-4-turbo")
        return ChatOpenAI(
            model=settings.OPENROUTER_MODEL,
            api_key=settings.OPENROUTER_API_KEY,
            base_url=settings.OPENROUTER_BASE_URL,
        )

    @classmethod
    def generate_story(cls, db: Session, session_id: str, theme: str = "fantasy") -> Story:
        llm = cls._get_llm()
        # pass a model into the pydantic output parser:
        story_parser = PydanticOutputParser(pydantic_object=StoryLLMResponse)

        prompt = ChatPromptTemplate.from_messages([
            (
                "system",
                STORY_PROMPT
            ),
            (
                "human",
                f"Create the story with this theme: {theme}"
            )
        # gives a str to the llm of what the response should look like:
        # pass the format_instructions to the Prompt
        ]).partial(format_instructions=story_parser.get_format_instructions()) 

        raw_response = llm.invoke(prompt.invoke({}))

        # make sure that the response is in right format:
        response_text = raw_response
        if hasattr(raw_response, "content"):
            response_text = raw_response.content
        
        story_structure = story_parser.parse(response_text)

        story_db = Story(title=story_structure.title, session_id=session_id)
        db.add(story_db)
        db.flush()

        root_node_data = story_structure.rootNode
        if isinstance(root_node_data, dict): # if its a dictionary, validate if node is correct format
            root_node_data = StoryNodeLLM.model_validate(root_node_data)
        
        cls._process_story_node(db, story_db.id, root_node_data, is_root=True)

        db.commit()
        return story_db
    
    # takes the root_node_data from generate_story and pass it here:
    @classmethod
    def _process_story_node(cls, db: Session, story_id: int, node_data: StoryNodeLLM, is_root: bool = False) -> StoryNode :
        
        # process the root node:
        node = StoryNode(
            story_id=story_id,
            content=node_data.content if hasattr(node_data, "content") else node_data["content"],
            is_root=is_root,
            is_ending=node_data.isEnding if hasattr(node_data, "isEnding") else node_data["isEnding"],
            is_winning_ending=node_data.isWinningEnding if hasattr(node_data, "isWinningEnding") else node_data["isWinningEnding"],
            options=[]
        )
        # add root node to the database:
        db.add(node)
        db.flush()

        # look for Options, if there's any
        if not node.is_ending and (hasattr(node_data, "options") and node_data.options):
            options_list = []
            # look for Options returned by LLM > convert to Node > and store in the Database:
            # loop through options passed from the Parameters "node_data: StoryNodeLLM" (not from node = StoryNode(...) object)
            for option_data in node_data.options:
                next_node = option_data.nextNode

                # is next_node valid for us to process?
                if isinstance(next_node, dict):
                    next_node = StoryNodeLLM.model_validate(next_node)
                
                # if yes, we process it same way as the root node:
                child_node = cls._process_story_node(db, story_id, next_node, False)

                options_list.append({
                    "text": option_data.text,
                    "node_id": child_node.id,
                })

                node.options = options_list
        db.flush()
        return node