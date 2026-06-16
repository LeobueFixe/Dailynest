from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from app.core.database import create_tables
from app.routers import api_router

# Create tables on startup
create_tables()

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check endpoint
@app.get("/")
def home():
    return FileResponse(Path("frontend/index.html"))

# Include all routers
app.include_router(api_router.router)