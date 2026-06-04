from fastapi import HTTPException, status
from sqlmodel import Session, select
from app.models.agenda_models import Agenda
from app.schemas.agenda_schema import AgendaCreate, AgendaUpdate


#Create new Event
def create_agenda(db: Session, data: AgendaCreate, current_user):
    agenda = Agenda(
        date=data.date,
        event=data.event,
        category=data.category,
        user_id=current_user.id
    )

    db.add(agenda)
    db.commit()
    db.refresh(agenda)
    return agenda

#Get Event by ID
def get_agenda_by_id(db: Session, agenda_id: int, current_user):
    agenda = db.get(Agenda, agenda_id)

    if not agenda:
        raise HTTPException(status_code=404, detail="Agenda entry not found")

    if agenda.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not allowed")

    return agenda

#Get all events
def get_agendas(db: Session, current_user):
    query = select(Agenda).where(Agenda.user_id == current_user.id)
    return db.exec(query).all()

#Update Event
def update_agenda(db: Session, agenda_id: int, data: AgendaUpdate, current_user):
    agenda = get_agenda_by_id(db, agenda_id, current_user)

    if data.date is not None:
        agenda.date = data.date

    if data.event is not None:
        agenda.event = data.event

    if data.category is not None:
        agenda.category = data.category

    db.add(agenda)
    db.commit()
    db.refresh(agenda)
    return agenda

#Delete Event
def delete_agenda(db: Session, agenda_id: int, current_user):
    agenda = get_agenda_by_id(db, agenda_id, current_user)

    db.delete(agenda)
    db.commit()
    return {"detail": "Agenda entry deleted successfully"}
