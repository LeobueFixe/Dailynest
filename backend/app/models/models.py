#database tables and relationships

from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)

    tasks = relationship("Task", back_populates="user", cascade="all, delete")
    agendas = relationship("Agenda", back_populates="user", cascade="all, delete")
    notepads = relationship("Notepad", back_populates="user", cascade="all, delete")
    files = relationship("File", back_populates="user", cascade="all, delete")


class Task(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True)
    description = Column(Text)
    user_id = Column(Integer, ForeignKey("user.id"))

    user = relationship("User", back_populates="tasks")


class Agenda(Base):
    __tablename__ = "agenda"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(String, nullable=False, index=True)
    event = Column(String, nullable=False, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))

    user = relationship("User", back_populates="agendas")


class File(Base):
    __tablename__ = "file"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, nullable=False, index=True)
    path = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"))

    user = relationship("User", back_populates="files")


class Notepad(Base):
    __tablename__ = "notepad"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True)
    content = Column(Text)
    user_id = Column(Integer, ForeignKey("user.id"))

    user = relationship("User", back_populates="notepads")  