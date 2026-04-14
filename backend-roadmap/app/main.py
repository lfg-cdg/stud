from fastapi import FastAPI

from app.routers import bookmarks, notes, projects

app = FastAPI(title="Notes API", version="0.1.0")
app.include_router(notes.router)
app.include_router(bookmarks.router)
app.include_router(projects.router)


@app.get("/")
def healthcheck():
    return {"status": "ok"}
