from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from db.database import Base

class Story(Base):
    __tablename__ = "stories"

    # just like how we query in SQL:
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    # to see stories created by a browser session:
    session_id = Column(String, index=True)
    # automatically grab current time:
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # one-to-many relationship, multiple nodes connected to 1 story
    nodes = relationship("StoryNode", back_populates="story")

# Different nodes or paths per story
class StoryNode(Base):
    __tablename__ = "story_nodes"

    id = Column(Integer, primary_key=True, index=True)
    story_id = Column(Integer, ForeignKey("stories.id"), index=True)
    content = Column(String)
    is_root = Column(Boolean, default=False)
    is_ending = Column(Boolean, default=False)
    is_winning_ending = Column(Boolean, default=False)
    options = Column(JSON, default=list)

    story = relationship("Story", back_populates="nodes")