from fastapi import FastAPI, HTTPException

from app.schemas import (
    BookmarkCreate,
    BookmarkUpdate,
    NoteCreate,
    NoteUpdate,
    ProjectCreate,
    ProjectUpdate,
    TagCreate,
    UserCreate,
)

app = FastAPI(title="Notes API", version="0.1.0")

notes = []
note_id_counter = 0

bookmarks = []
bookmark_id_counter = 0

projects = []
project_id_counter = 0


@app.get("/")
def healthcheck():
    return {"status": "ok"}


@app.post("/notes", status_code=201)
def create_note(note: NoteCreate):
    global note_id_counter
    note_id_counter += 1

    created_note = {"id": note_id_counter, **note.model_dump()}
    notes.append(created_note)

    return {"message": "Note created successfully!", "note": created_note}


@app.get("/notes")
def check_notes():
    return {"notes": notes}


@app.get("/notes/{note_id}")
def check_note_by_id(note_id: int):
    for note in notes:
        if note["id"] == note_id:
            return note

    raise HTTPException(status_code=404, detail="Note not found")


@app.delete("/notes/{note_id}", status_code=200)
def delete_note(note_id: int):
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            return {"message": "Note deleted!"}

    raise HTTPException(status_code=404, detail="Note not found")


@app.put("/notes/{note_id}")
def update_note(note_id: int, new_note: NoteUpdate):
    for note in notes:
        if note["id"] == note_id:
            note.update(new_note.model_dump())
            return note

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


@app.post("/bookmarks", status_code=201)
def create_bookmark(bookmark: BookmarkCreate):
    global bookmark_id_counter
    bookmark_id_counter += 1

    created_bookmark = {"id": bookmark_id_counter, **bookmark.model_dump()}
    bookmarks.append(created_bookmark)
    return {"message": "Bookmark created", "bookmark": created_bookmark}


@app.get("/bookmarks")
def check_bookmarks():
    return bookmarks


@app.get("/bookmarks/favourite")
def check_favourite_bookmarks():
    favourite = []

    for bookmark in bookmarks:
        if bookmark["is_favourite"]:
            favourite.append(bookmark)

    return favourite


@app.get("/bookmarks/{bookmark_id}")
def check_bookmark_by_id(bookmark_id: int):
    for bookmark in bookmarks:
        if bookmark["id"] == bookmark_id:
            return bookmark

    raise HTTPException(status_code=404, detail="Bookmark not found")


@app.put("/bookmarks/{bookmark_id}")
def update_bookmark(bookmark_id: int, updated_bookmark: BookmarkUpdate):
    for bookmark in bookmarks:
        if bookmark["id"] == bookmark_id:
            bookmark.update(updated_bookmark.model_dump())
            return bookmark

    raise HTTPException(status_code=404, detail="Bookmark not found")


@app.delete("/bookmarks/{bookmark_id}")
def delete_bookmark(bookmark_id: int):
    for bookmark in bookmarks:
        if bookmark["id"] == bookmark_id:
            bookmarks.remove(bookmark)
            return {"message": "Bookmark deleted"}

    raise HTTPException(status_code=404, detail="Bookmark not found")


@app.post("/projects", status_code=201)
def create_project(project: ProjectCreate):
    global project_id_counter
    project_id_counter += 1

    created_project = {"id": project_id_counter, **project.model_dump()}
    projects.append(created_project)

    return created_project


@app.get("/projects")
def check_projects():
    return projects


@app.get("/projects/{project_id}")
def check_project_by_id(project_id: int):
    for project in projects:
        if project["id"] == project_id:
            return project

    raise HTTPException(status_code=404, detail="Project not found")


@app.put("/projects/{project_id}")
def update_projects(project_id: int, new_project: ProjectUpdate):
    for project in projects:
        if project["id"] == project_id:
            project.update(new_project.model_dump())
            return new_project

    raise HTTPException(status_code=404, detail="Project not found")


@app.delete("/projects/{projects_id}")
def delete_project(project_id: int):
    for project in projects:
        if project["id"] == project_id:
            projects.remove(project)
            return {"message": "Project deleted!"}

    raise HTTPException(status_code=404, detail="Project not found")
