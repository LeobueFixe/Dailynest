from fastapi import HTTPException
from sqlmodel import Session, select
from app.models.notepad_models import Notepad
from app.schemas.notepad_schema import NotepadCreate, NotepadUpdate


#Create Note
def create_notepad(db: Session, data: NotepadCreate, current_user):
    notepad = Notepad(
        title=data.title,
        content=data.content,
        category=data.category,
        user_id=current_user.id
    )

    db.add(notepad)
    db.commit()
    db.refresh(notepad)
    return notepad

#Get Note by ID
def get_notepad_by_id(db: Session, notepad_id: int, current_user):
    notepad = db.get(Notepad, notepad_id)

    if not notepad:
        raise HTTPException(status_code=404, detail="Notepad entry not found")

    if notepad.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not allowed")

    return notepad    

#Get all Notes
def get_notepads(db: Session, current_user):
    query = select(Notepad).where(Notepad.user_id == current_user.id)
    return db.exec(query).all()

#Update Note
def update_notepad(db: Session, notepad_id: int, data: NotepadUpdate, current_user):
    notepad = get_notepad_by_id(db, notepad_id, current_user)

    if data.title is not None:
        notepad.title = data.title

    if data.content is not None:
        notepad.content = data.content

    if data.category is not None:
        notepad.category = data.category

    db.add(notepad)
    db.commit()
    db.refresh(notepad)
    return notepad

#Delete Note
def delete_notepad(db: Session, notepad_id: int, current_user):
    notepad = get_notepad_by_id(db, notepad_id, current_user)

    db.delete(notepad)
    db.commit()
    return {"detail": "Notepad entry deleted successfully"}
