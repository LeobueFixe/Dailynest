from datetime import datetime, timedelta
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from sqlmodel import Session, select
import jwt
from app.models.user_models import User
from app.schemas.user_schema import UserCreate, Token, TokenData
from app.core.config import settings
from app.core.database import get_session

#Password Hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

#Verify the password
def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)

#Create token
def create_access_token(data: dict, expires_minutes: int = settings.ACCESS_TOKEN_EXPIRE_MINUTES):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=expires_minutes)
    to_encode.update({"exp": expire})

    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

#Create Account
def register_user(db: Session, data: UserCreate):
    # Check if email exists
    existing = db.exec(select(User).where(User.email == data.email)).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    user = User(
        name=data.name,
        email=data.email,
        password=hash_password(data.password)
    )

    db.add(user)
    db.commit()
    db.refresh(user)
    return user

#Authentication
def authenticate_user(db: Session, email: str, password: str):
    user = db.exec(select(User).where(User.email == email)).first()

    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    return user

#Get User by token
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_session)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_id: int = payload.get("sub")

        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")

        token_data = TokenData(user_id=user_id)

    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token Expired")

    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid Token")
    
    #Load User
    user = db.get(User, token_data.user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user

#Login
def login_user(db: Session, email: str, password: str):
    user = authenticate_user(db, email, password)
    access_token = create_access_token({"sub": str(user.id)})

    return Token(access_token=access_token)
