from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.config import settings

app = FastAPI(
    title="Choose Your Own Adventure Game API",
    description="api to generate cool stories",
    version="0.1.0", # for versioning every time we make a change in prod
    #for documentation:
    docs_url="/docs",
    redoc_url="/redoc",
)

# to use api from diff. origin like from port: 8000 to use in port: 5173
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True, # allow us to send credentials to our backend
    allow_methods=["*"], # allow to use different types of methods (GET, POST, etc.)
    allow_headers=["*"], 
)

if __name__ == "__main__":
    # uvicorn = web server
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)