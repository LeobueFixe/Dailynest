from fastapi import HTTPException
from sqlmodel import Session, select
from app.models.user_models import User
from app.schemas.user_schema import UserUpdate


#Get User by ID
def get_user_by_id(db: Session, user_id: int):
    user = db.get(User, user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user

#Get Profile
def get_profile(db: Session, current_user):
    return get_user_by_id(db, current_user.id)

#Update account
def update_user(db: Session, data: UserUpdate, current_user):
    user = get_user_by_id(db, current_user.id)

    #Confirm email
    if data.email and data.email != user.email:
        existing = db.exec(select(User).where(User.email == data.email)).first()
        if existing:
            raise HTTPException(status_code=400, detail="Email already in use")

        user.email = data.email

    if data.name is not None:
        user.name = data.name

    if data.password is not None:
        #Hash password
        user.password = data.password

    db.add(user)
    db.commit()
    db.refresh(user)
    return user

#Delete Account
def delete_user(db: Session, current_user):
    user = get_user_by_id(db, current_user.id)

    db.delete(user)
    db.commit()
    return {"detail": "User account deleted successfully"}