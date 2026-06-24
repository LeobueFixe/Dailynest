from typing import Optional
from sqlmodel import Field, SQLModel, Relationship


class Notepad(SQLModel, table=True):
    __tablename__ = "notepads"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(index=True, max_length=100)
    content: Optional[str] = None
    category: str = Field(default="Personal", max_length=50)
    
    user_id: int = Field(foreign_key="users.id", nullable=False)
    user: Optional["User"] = Relationship(back_populates="notepads")
