from fastapi import FastAPI

from .schemas import NoteCreate

app = FastAPI(title="Notes API", version="0.1.0")


@app.get("/")
def healthcheck():
    return {"status": "ok"}


@app.post("/notes", status_code=201)
def create_note(note: NoteCreate):
    return {"message": "Note created!", "note": note.model_dump()}
