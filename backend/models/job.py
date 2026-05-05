# Represents the Intent to make a story and has a progress, like In Progress, Finished, etc.

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from db.database import Base

class StoryJob(Base):
    __tablename__ = "story_jobs"

    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(String, index=True, unique=True)
    session_id = Column(String, index=True)
    theme = Column(String)
    status = Column(String)
    story_id = Column(Integer, nullable=True) # nullable=True means it can have Null or No Value
    error = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    completed_at = Column(DateTime(timezone=True), nullable=True) # how long the job took, nullable=True because the job might fail and never finish