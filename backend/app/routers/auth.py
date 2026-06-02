from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.dependencies import get_db
from app.schemas.user import UserCreate, UserResponse, UserLogin
from app.services.user_service import create_user, authenticate_user

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
def login(payload: UserLogin, db: Session = Depends(get_db)):
    user = authenticate_user(db, payload.email, payload.password)

    if not user:
        return {"error": "invalid credentials"}

    return {
        "message": "login success",
        "user_id": user.id
    }

@router.post("/register")
def register(payload: UserCreate, db: Session = Depends(get_db)):
    user = create_user(
        db,
        payload.name,
        payload.email,
        payload.password
    )

    return {
        "id": user.id,
        "name": user.name,
        "email": user.email
    }