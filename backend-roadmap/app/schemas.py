from pydantic import BaseModel


class NoteCreate(BaseModel):
    title: str
    content: str
    tags: list[str] = []


class TagCreate(BaseModel):
    name: str


class UserCreate(BaseModel):
    username: str
    email: str
    age: int
