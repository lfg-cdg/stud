import pytest

from app.schemas import NoteCreate


@pytest.fixture
def sample_note():
    return NoteCreate(title="Note1", content="Sample note for test")


def test_note_create_correct(sample_note):
    assert sample_note.title == "Note1"
    assert sample_note.content == "Sample note for test"
    assert sample_note.tags == []
