# Structure of data, we specify the type of data our API accepts and returns
# Each class below subclasses pydantic.BaseModel so field types are validated and serialized (not just hints).

from typing import List, Optional, Dict
from datetime import datetime
from pydantic import BaseModel

class StoryOptionsSchema(BaseModel):
    # One branch choice from a node; shown to the client as an option they can pick
    text: str
    node_id: Optional[int] = None  # id of the next node when this option is chosen; None if unset

class StoryNodeBase(BaseModel):  # not used directly to the API,
    # Shared fields for any "node" shape; subclasses add id/options for API responses
    content: str
    is_ending: bool = False
    is_winning_ending: bool = False

class CompleteStoryNodeResponse(StoryNodeBase):  # "Response", its what's returned to the frontend
    id: int
    options: List[StoryOptionsSchema] = []  # outgoing choices from this node

    class Config:
        # Allow constructing from ORM rows (e.g. SQLAlchemy) via attribute access, not only dicts
        from_attributes = True

class StoryBase(BaseModel):
    # Shared story metadata; extended by full story responses
    title: str
    session_id: Optional[str] = None  # optional client/session correlation

    class Config:
        from_attributes = True

class CreateStoryRequest(BaseModel):
    # Body for POST (or similar) when creating a new story
    theme: str


class CompleteStoryResponse(StoryBase):
    # Full story graph for the frontend: root + lookup table of every node by id
    id: int
    created_at: datetime
    root_node: CompleteStoryNodeResponse
    all_nodes: Dict[int, CompleteStoryNodeResponse]

    class Config:
        from_attributes = True