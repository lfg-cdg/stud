from fastapi import FastAPI, HTTPException

from app.schemas import NoteCreate, NoteUpdate, TagCreate, UserCreate

app = FastAPI(title="Notes API", version="0.1.0")
notes = []
note_id_counter = 0


@app.get("/")
def healthcheck():
    return {"status": "ok"}


@app.post("/notes", status_code=201)
def create_note(note: NoteCreate):
    global note_id_counter
    note_id_counter += 1

    created_note = {"id": note_id_counter, "note": note.model_dump()}
    notes.append(created_note)

    return {"message": "Note created successfully!", "note": notes}


@app.get("/notes")
def check_notes():
    return {"notes": notes}


@app.get("/notes/{note_id}")
def check_note_by_id(note_id: int):
    for note in notes:
        if note["id"] == note_id:
            return {note}
        
        else: 
            raise HTTPException(status_code=404, detail="Note not found")
            

@app.delete("/notes/{note_id}", status_code=200)
def delete_note(note_id: int):
    for note in notes:
        if note["id"] == note_id:
            return {note}
        else:
            raise HTTPException(status_code=404, detail="Note not found")
        
@app.put("/notes/{note_id}")
def update_note(note_id: int, new_note: NoteUpdate):
    for note in notes:
        if note["id"] == note_id:
            note = new_note
            return {new_note}
        else:
            raise HTTPException(status_code=404, detail="Note not found")

@app.post("/tags", status_code=201)
def create_tag(tag: TagCreate):
    return {"message": "Tag created!", "tag": tag.model_dump()}


@app.get("/tags")
def check_tags():
    return {"tags": []}


@app.post("/users", status_code=201)
def create_user(user: UserCreate):
    return {"message": "User created", "user": user.model_dump()}


@app.get("/users")
def check_users():
    return {"users": []}


@app.get("/users/{user_id}")
def check_user_by_id(user_id: int):
    return {"user_id": user_id, "username": "Jopa228"}
