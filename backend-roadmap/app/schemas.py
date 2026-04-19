from pydantic import BaseModel


class NoteCreate(BaseModel):
    title: str
    content: str
    is_complete: bool = False


class NoteUpdate(BaseModel):
    title: str
    content: str
    is_complete: bool = False


class NoteResponse(BaseModel):
    id: int
    title: str
    content: str
    is_complete: bool

    model_config = {"from_attributes": True}


class BookmarkCreate(BaseModel):
    title: str
    url: str
    is_favourite: bool = False


class BookmarkUpdate(BaseModel):
    title: str
    url: str
    is_favourite: bool = False


class BookmarkResponse(BaseModel):
    id: int
    title: str
    url: str
    is_favourite: bool

    model_config = {"from_attributes": True}


class ProjectCreate(BaseModel):
    title: str
    description: str
    is_done: bool = False


class ProjectUpdate(BaseModel):
    title: str
    description: str
    is_done: bool = False


class ProjectResponse(BaseModel):
    id: int
    title: str
    description: str
    is_done: bool

    model_config = {"from_attributes": True}


class CreateTask(BaseModel):
    title: str
    content: str
    is_complete: bool = False


class UpdateTask(BaseModel):
    title: str
    content: str
    is_complete: bool = False
