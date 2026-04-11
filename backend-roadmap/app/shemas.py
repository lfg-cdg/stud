from dataclasses import dataclass, field


@dataclass(slots=True)
class NoteCreate:
    title: str
    content: str
    tags: list[str] = field(default_factory=list)
