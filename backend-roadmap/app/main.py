from fastapi import FastAPI

from app.schemas import NoteCreate, TagCreate, UserCreate

app = FastAPI(title="Notes API", version="0.1.0")


@app.get("/")
def healthcheck():
    return {"status": "ok"}


@app.post("/notes", status_code=201)
def create_note(note: NoteCreate):
    return {"message": "Note created!", "note": note.model_dump()}


@app.get("/notes")
def check_notes():
    return {"notes": []}


@app.get("/notes/{note_id}")
def check_note_by_id(note_id: int):
    return {"note_id": note_id, "title": "Jopa"}


@app.post("/tags", status_code=201)
def create_tag(tag: TagCreate):
    return {"message": "Tag created!", "tag": tag.model_dump()}


@app.get("/tags")
def check_tags():
    return {"tags": []}


@app.delete("/notes/{note_id}", status_code=200)
def delete_note(note_id: int):
    return {"message": "Note deleted!", "note_id": note_id}


@app.post("/users", status_code=201)
def create_user(user: UserCreate):
    return {"message": "User created", "user": user.model_dump()}


@app.get("/users")
def check_users():
    return {"users": []}


@app.get("/users/{user_id}")
def check_user_by_id(user_id: int):
    return {"user_id": user_id, "username": "Jopa228"}
