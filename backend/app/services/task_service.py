from fastapi import HTTPException, status
from sqlmodel import Session, select
from app.models.task_models import Task
from app.schemas.task_schema import TaskCreate, TaskUpdate


#Create Task
def create_task(db: Session, data: TaskCreate, current_user):
    task = Task(
        title=data.title,
        description=data.description,
        category=data.category,
        user_id=current_user.id
    )

    db.add(task)
    db.commit()
    db.refresh(task)
    return task

#Get Task by ID
def get_task_by_id(db: Session, task_id: int, current_user):
    task = db.get(Task, task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    if task.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not allowed")
    
    return task

#Get all Tasks
def get_tasks(db: Session, current_user):
    query = select(Task).where(Task.user_id == current_user.id)
    return db.exec(query).all()

#Update Task
def update_task(db: Session, task_id: int, data: TaskUpdate, current_user):
    task = get_task_by_id(db, task_id, current_user)

    if data.title is not None:
        task.title = data.title

    if data.description is not None:
        task.description = data.description

    if data.category is not None:
        task.category = data.category
    
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

#Delete Task
def delete_task(db: Session, task_id: int, current_user):
    task = get_task_by_id(db, task_id, current_user)

    db.delete(task)
    db.commit()
    return {"detail": "Task deleted successfully"}