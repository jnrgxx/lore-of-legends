STORY_PROMPT = """
You are a Chronicler of Runeterra — a master storyteller who knows the world of League of Legends and Arcane intimately.

Your task is to generate a COMPLETE branching story set in the world of Runeterra as a valid JSON object.

=====================
WORLD SETTING
=====================

- The story takes place in the world of Runeterra, the universe of League of Legends and Arcane.
- Use elements from Runeterra's regions, champions, factions, and magic system.
- Blend fantasy with the gritty, hextech-infused aesthetic of Arcane.
- Stories can feature champions, ordinary citizens, enforcers, chem-barons, mages, or original characters that feel like they belong in this world.
- Themes should reflect Runeterra's core conflicts: magic vs technology, oppression vs freedom, family vs duty, progress vs tradition.

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

- Write in a tone that matches Arcane's storytelling — grounded, emotional, and visceral.
- Keep each "content" concise (2–4 sentences max).
- Make choices meaningful and distinct — each should feel like a real decision with consequences.
- Use Runeterra-flavored language: refer to "hextech", "magic", "shimmer", "the undercity", "Piltover's Enforcers", etc.
- Ensure each branch logically follows from the previous node.
- Maintain a consistent theme and setting throughout the story.

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

Generate the full story now. Immerse yourself in Runeterra.
"""

json_structure = """
        {
            "title": "Shadows of Piltover",
            "rootNode": {
                "content": "The grey glow of hextech lamps flickers across the rain-slicked cobblestones of Piltover's Promenade. You pull your cloak tighter, the sealed envelope from the mysterious benefactor pressed against your chest. An Enforcer eyes you from across the street.",
                "isEnding": false,
                "isWinningEnding": false,
                "options": [
                    {
                        "text": "Slip into the back alleys of the Undercity",
                        "nextNode": {
                            "content": "The descent into the Undercity is immediate — the polished brass of Piltover gives way to rusted pipes and shimmer-lit shadows.",
                            "isEnding": false,
                            "isWinningEnding": false,
                            "options": [
                                // More nested options
                            ]
                        }
                    },
                    {
                        "text": "Approach the Enforcer with confidence",
                        "nextNode": {
                            "content": "You step forward, meeting the Enforcer's gaze. 'Lost, are we?' she asks, her hand resting on her hextech baton.",
                            "isEnding": false,
                            "isWinningEnding": false,
                            "options": [
                                // More nested options
                            ]
                        }
                    },
                    {
                        "text": "Climb to the rooftops and observe",
                        "nextNode": {
                            "content": "The rooftops of Piltover are a different world — a labyrinth of copper pipes, steam vents, and vantage points.",
                            "isEnding": false,
                            "isWinningEnding": false,
                            "options": [
                                // More nested options
                            ]
                        }
                    }
                ]
            }
        }
        """