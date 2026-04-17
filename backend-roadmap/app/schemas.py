from pydantic import BaseModel


class NoteCreate(BaseModel):
    title: str
    content: str
    tags: list[str] = []
    is_complete: bool = False


class NoteUpdate(BaseModel):
    title: str
    content: str
    tags: list[str] = []
    is_complete: bool = False


class BookmarkCreate(BaseModel):
    url: str
    title: str
    is_favourite: bool = False


class BookmarkUpdate(BaseModel):
    url: str
    title: str
    is_favourite: bool = False


class ProjectCreate(BaseModel):
    name: str
    description: str
    is_active: bool = True


class ProjectUpdate(BaseModel):
    name: str
    description: str
    is_active: bool = True


class CreateTask(BaseModel):
    title: str
    content: str
    is_complete: bool = False


class UpdateTask(BaseModel):
    title: str
    content: str
    is_complete: bool = False
