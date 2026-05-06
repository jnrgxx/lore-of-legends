# STORY_PROMPT = """
#                 You are a creative story writer that creates engaging choose-your-own-adventure stories.
#                 Generate a complete branching story with multiple paths and endings in the JSON format I'll specify.

#                 CRITICAL: Every non-ending node MUST contain exactly 2-3 options in the "options" array.
#                 A node with only 1 option makes the story linear and defeats the purpose of a branching adventure.
                

#                 The story should have:
#                 1. A compelling title
#                 2. A starting situation (root node) with 2-3 options
#                 3. Each option should lead to another node with its own options
#                 4. Some paths should lead to endings (both winning and losing)
#                 5. At least one path should lead to a winning ending

#                 Story structure requirements:
#                 - Each node should have 2-3 options except for ending nodes
#                 - The story should be 3-4 levels deep (including root node)
#                 - Add variety in the path lengths (some end earlier, some later)
#                 - Make sure there's at least one winning path

#                 Output your story in this exact JSON structure:
#                 {format_instructions}

#                 Don't simplify or omit any part of the story structure. 
#                 Don't add any text outside of the JSON structure.
#                 """

STORY_PROMPT = """
You are a structured story generation engine for a choose-your-own-adventure game.

Your task is to generate a COMPLETE branching story as a valid JSON object.

=====================
CORE REQUIREMENTS
=====================

- The story MUST follow a strict tree structure.
- The root node starts the story.
- Each non-ending node MUST have EXACTLY 2 or 3 options.
- Ending nodes MUST have:
  - "isEnding": true
  - "isWinningEnding": true or false
  - NO "options" field OR an empty array

- The story depth MUST be between 3 and 4 levels (root included).
- Include a mix of:
  - early endings
  - deeper branches
- At least ONE path MUST lead to a winning ending.

=====================
WRITING REQUIREMENTS
=====================

- Keep each "content" concise (2–4 sentences max).
- Make choices meaningful and distinct.
- Ensure each branch logically follows from the previous node.
- Maintain a consistent theme throughout the story.

=====================
STRICT JSON RULES (CRITICAL)
=====================

- Output ONLY valid JSON.
- DO NOT include explanations, comments, or markdown.
- DO NOT include trailing commas.
- DO NOT include "//" comments.
- ALL keys and strings MUST use double quotes.
- Ensure the JSON is fully parsable.

=====================
OUTPUT FORMAT
=====================

Use this exact structure:

{format_instructions}

=====================
VALIDATION RULES (VERY IMPORTANT)
=====================

Before finishing:
- Ensure EVERY non-ending node has 2–3 options.
- Ensure NO node has only 1 option.
- Ensure at least one node has "isWinningEnding": true.
- Ensure all branches terminate correctly.
- Ensure JSON is valid and complete.

Generate the full story now.
"""

json_structure = """
        {
            "title": "Story Title",
            "rootNode": {
                "content": "The starting situation of the story",
                "isEnding": false,
                "isWinningEnding": false,
                "options": [
                    {
                        "text": "Option 1 text",
                        "nextNode": {
                            "content": "What happens for option 1",
                            "isEnding": false,
                            "isWinningEnding": false,
                            "options": [
                                // More nested options
                            ]
                        }
                    },
                    {
                        "text": "Option 2 text",
                        "nextNode": {
                            "content": "What happens for option 2",
                            "isEnding": false,
                            "isWinningEnding": false,
                            "options": [
                                // More nested options
                            ]
                        }
                    },
                    {
                        "text": "Option 3 text",
                        "nextNode": {
                            "content": "What happens for option 3",
                            "isEnding": false,
                            "isWinningEnding": false,
                            "options": [
                                // More nested options
                            ]
                        }
                    },
                    // More options for root node
                ]
            }
        }
        """