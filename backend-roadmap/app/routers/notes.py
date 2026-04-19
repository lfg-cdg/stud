from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Note
from app.schemas import NoteCreate, NoteUpdate

router = APIRouter(prefix="/notes", tags=["Notes"])


def get_note_or_404(note_id: int, db: Session = Depends(get_db)) -> Note:
    note = db.query(Note).filter(Note.id == note_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@router.post("/", status_code=201)
def create_note(note: NoteCreate, db: Session = Depends(get_db)):
    new_note = Note(**note.model_dump())

    db.add(new_note)
    db.commit()
    db.refresh(new_note)

    return new_note


@router.get("/")
def check_notes(db: Session = Depends(get_db)):
    notes = db.query(Note).all()
    return notes


@router.get("/completed")
def check_completed_notes(db: Session = Depends(get_db)):
    completed_notes = db.query(Note).filter(Note.is_complete.is_(True)).all()
    return completed_notes


@router.get("/{note_id}")
def check_note_by_id(note_id: int, db: Session = Depends(get_db)):
    return get_note_or_404(note_id, db)


@router.delete("/{note_id}", status_code=200)
def delete_note(note_id: int, db: Session = Depends(get_db)):
    note = get_note_or_404(note_id, db)

    db.delete(note)
    db.commit()

    return {"message": "Note deleted!"}


@router.put("/{note_id}")
def update_note(note_id: int, new_note: NoteUpdate, db: Session = Depends(get_db)):
    note = get_note_or_404(note_id, db)

    for key, value in new_note.model_dump().items():
        setattr(note, key, value)

    db.commit()
    db.refresh(note)

    return note


@router.put("/{note_id}/complete")
def update_note_status(note_id: int, db: Session = Depends(get_db)):
    note = get_note_or_404(note_id, db)

    note.is_complete = True
    db.commit()
    db.refresh(note)

    return note
