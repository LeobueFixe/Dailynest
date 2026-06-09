from fastapi import HTTPException
from sqlmodel import Session, select
from app.models.file_models import File
from app.schemas.file_schema import FileCreate, FileUpdate


#Create File
def create_file(db: Session, data: FileCreate, current_user):
    file = File(
        filename=data.filename,
        filepath=data.filepath,
        category=data.category,
        user_id=current_user.id
    )

    db.add(file)
    db.commit()
    db.refresh(file)
    return file

#Get File by ID
def get_file_by_id(db: Session, file_id: int, current_user):
    file = db.get(File, file_id)

    if not file:
        raise HTTPException(status_code=404, detail="File not found")

    if file.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not allowed")

    return file

#Get all Files
def get_files(db: Session, current_user):
    query = select(File).where(File.user_id == current_user.id)
    return db.exec(query).all()

#Update File
def update_file(db: Session, file_id: int, data: FileUpdate, current_user):
    file = get_file_by_id(db, file_id, current_user)

    if data.filename is not None:
        file.filename = data.filename

    if data.filepath is not None:
        file.filepath = data.filepath

    if data.category is not None:
        file.category = data.category

    db.add(file)
    db.commit()
    db.refresh(file)
    return file

#Delete File
def delete_file(db: Session, file_id: int, current_user):
    file = get_file_by_id(db, file_id, current_user)

    db.delete(file)
    db.commit()
    return {"detail": "File deleted successfully"}
