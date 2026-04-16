from pydantic import BaseModel


class NoteCreate(BaseModel):
    title: str
    content: str
    tags: list[str] = []


class NoteUpdate(BaseModel):
    title: str
    content: str
    tags: list[str] = []


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
