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
    is_favourite: bool = True


class BookmarkUpdate(BaseModel):
    title: str
    url: str
    is_favourite: bool = True


class BookmarkResponse(BaseModel):
    id: int
    title: str
    url: str
    is_favourite: bool = True

    model_config = {"from_attributes": True}


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
