from fastapi import APIRouter
from app.routers import agenda_router, auth_router, file_router, notepad_router, task_router, user_router

router = APIRouter(prefix="/api", tags=["API"])

subRouters = [auth_router, user_router, task_router, agenda_router, notepad_router, file_router]

for sRouter in subRouters:
    router.include_router(sRouter.router)