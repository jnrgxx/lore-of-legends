from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field, model_validator

# Structure of the Story
# Detailed Class on how we want the LLM to give us the data

class StoryOptionLLM(BaseModel):
    text: str = Field(description="the text of the option shown to the user")
    nextNode: Dict[str, Any] = Field(description="the next node content and its options")

class StoryNodeLLM(BaseModel):
    content: str = Field(description="The main content of the story node")
    isEnding: bool = Field(description="Whether this node is an ending node")
    isWinningEnding: bool = Field(description="Whether this node is a winning ending node")
    options: Optional[List[StoryOptionLLM]] = Field(default=None, min_length=2, description="The options for this node")
    
    @model_validator(mode="after")
    def validate_options(self) -> "StoryNodeLLM":
        if self.isEnding:
            self.options = None  # ending nodes should never have options
        elif not self.options or len(self.options) < 2:
            raise ValueError(
                f"Non-ending nodes must have at least 2 options, got {len(self.options or [])}"
            )
        return self
class StoryLLMResponse(BaseModel):
    title: str = Field(description="The title of the story")
    rootNode: StoryNodeLLM = Field(description="The root node of the story")