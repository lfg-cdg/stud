from fastapi import APIRouter, HTTPException

from app.schemas import NoteCreate, NoteUpdate

router = APIRouter(prefix="/notes", tags=["Notes"])

notes = []
note_id_counter = 0


@router.post("/", status_code=201)
def create_note(note: NoteCreate):
    global note_id_counter
    note_id_counter += 1

    created_note = {"id": note_id_counter, **note.model_dump()}
    notes.append(created_note)

    return {"message": "Note created successfully!", "note": created_note}


@router.get("/")
def check_notes():
    return {"notes": notes}


@router.get("/completed")
def check_completed_notes():
    completed_notes = []
    for note in notes:
        if note["is_complete"]:
            completed_notes.append(note)

    if not completed_notes:
        return HTTPException(status_code=404, detail="Not found done tasks")

    return completed_notes


@router.get("/{note_id}")
def check_note_by_id(note_id: int):
    for note in notes:
        if note["id"] == note_id:
            return note

    raise HTTPException(status_code=404, detail="Note not found")


@router.delete("/{note_id}", status_code=200)
def delete_note(note_id: int):
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            return {"message": "Note deleted!"}

    raise HTTPException(status_code=404, detail="Note not found")


@router.put("/{note_id}")
def update_note(note_id: int, new_note: NoteUpdate):
    for note in notes:
        if note["id"] == note_id:
            note.update(new_note.model_dump())
            return note

    raise HTTPException(status_code=404, detail="Note not found")


@router.put("/{note_id}/complete")
def update_note_status(note_id: int):
    for note in notes:
        if note["id"] == note_id:
            note["is_complete"] = True
            return note

    raise HTTPException(status_code=404, detail="Note not found")
