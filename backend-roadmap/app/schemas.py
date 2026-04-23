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


class NotePatch(BaseModel):
    title: str | None = None
    content: str | None = None
    is_complete: bool | None = None


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


class BookmarkPatch(BaseModel):
    title: str | None = None
    url: str | None = None
    is_favourite: bool | None = None


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


class ProjectPatch(BaseModel):
    title: str | None = None
    description: str | None = None
    is_done: bool | None = None


class CreateTask(BaseModel):
    title: str
    description: str
    priority: str
    is_done: bool = False


class UpdateTask(BaseModel):
    title: str
    description: str
    priority: str
    is_done: bool = False


class PatchTask(BaseModel):
    title: str | None = None
    description: str | None = None
    priority: str | None = None
    is_done: bool | None = None


class ResponseTask(BaseModel):
    id: int
    title: str
    description: str
    priority: str
    is_done: bool

    model_config = {"from_attributes": True}
