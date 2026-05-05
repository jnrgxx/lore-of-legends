import uuid
from typing import Optional
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, Cookie, Response, BackgroundTasks
from sqlalchemy.orm import Session

from db.database import get_db, SessionLocal
from models.story import Story, StoryNode
from models.job import StoryJob
from schemas.story import (
    CompleteStoryResponse, CompleteStoryNodeResponse, CreateStoryRequest
)
from schemas.job import StoryJobResponse

router = APIRouter(
    prefix="/stories",
    tags=["stories"]
)

def get_session_id(session_id: Optional[str] = Cookie(None)): # look for session_id, create if there's no session_id
    if not session_id:
        session_id = str(uuid.uuid4())
    return session_id

@router.post("/create", response_model=StoryJobResponse) # return a StoryJobResponse
def create_story (
    request: CreateStoryRequest, # accept a CreateStoryRequest
    background_tasks: BackgroundTasks,
    response: Response,
    session_id: str = Depends(get_session_id), # calls a function everytime the route is hit and get it's value
    db: Session = Depends(get_db)
):
    response.set_cookie(key="session_id", value=session_id, httponly=True)

    job_id = str(uuid.uuid4())

    # sends this to frontend immediately:
    job = StoryJob(
        job_id=job_id,
        session_id=session_id,
        theme=request.theme, # from CreateStoryRequest
        status="pending"
    )

    db.add(job) # like staging in git
    db.commit()

    # add background task, and this will run generate_story_task function
    background_tasks.add_task(
        generate_story_task,
        job_id=job_id,
        theme=request.theme,
        session_id=session_id
    )

    return job # returns job immediately

# runs this in the background:
def generate_story_task(job_id: str, theme: str, session_id: str):
    # Asynchronous Operation, creates a new database session, so we don't use the same session from create_story function so we don't have to wait
    db = SessionLocal()

    try:
        job = db.query(StoryJob).filter(StoryJob.job_id == job_id).first()

        if not job:
            return
        
        try:
            job.status = "processing"
            db.commit()

            story = {}  # todo: generate story

            job.story_id = 1 # todo: update story id
            job.status = "completed"
            job.completed_at = datetime.now()
            db.commit()

        except Exception as e:
            job.status = "failed"
            job.completed_at = datetime.now()
            job.error = str(e)
            db.commit()
    finally:
        db.close()

#@router.get(f"/{story_id}/complete", response_model=CompleteStoryResponse)
@router.get("/{story_id}/complete", response_model=CompleteStoryResponse)
def get_complete_story(story_id: int, db: Session = Depends(get_db)):
        # look for the story if it exists:
        story = db.query(Story).filter(Story.id == story_id).first()

        if not story:
            raise HTTPException(status_code=404, details="Story not found")
        
        complete_story = build_complete_story_tree(db, story)
        return complete_story

def build_complete_story_tree(db: Session, story: Story) -> CompleteStoryResponse:
    pass
