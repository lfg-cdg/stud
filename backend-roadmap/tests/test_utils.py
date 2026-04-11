import pytest

from app.exceptions import ValidationError
from app.utils import is_blank, normalize_title, validate_title


@pytest.mark.parametrize(
    "title, result",
    [
        ("  jopa  ", "jopa"),
        ("  ", ""),
        (" hello my name ", "hello my name"),
    ],
)
def test_normalize_title_strip_spaces(title, result):
    assert normalize_title(title) == result


@pytest.mark.parametrize(
    "value, result",
    [
        ("jopa", False),
        ("   ", True),
        ("", True),
        ("  jopa  ", False),
    ],
)
def test_is_value_blank(value, result):
    assert is_blank(value) == result


def test_validate_title_valid():
    assert validate_title("jopa") == "jopa"


def test_validate_title_blank():
    with pytest.raises(ValidationError):
        validate_title("   ")


def test_validate_title_too_long():
    with pytest.raises(ValidationError):
        validate_title(
            "12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901"
        )
