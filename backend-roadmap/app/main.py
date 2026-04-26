from fastapi import FastAPI

from app import models  # noqa: F401
from app.routers import bookmarks, notes, projects, tasks

app = FastAPI(title="Notes API", version="0.1.0")
app.include_router(notes.router)
app.include_router(bookmarks.router)
app.include_router(projects.router)
app.include_router(tasks.router)


@app.get("/")
def healthcheck():
    return {"status": "ok"}
