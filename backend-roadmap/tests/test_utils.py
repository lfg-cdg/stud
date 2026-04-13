import pytest

from app.exceptions import ValidationError
from app.utils import is_blank, normalize_title, validate_content, validate_email, validate_title


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


@pytest.mark.parametrize(
    "content, result",
    [
        ("   hello   ", "hello"),
        (" hello world", "hello world"),
    ],
)
def test_validate_content_strip(content, result):
    assert validate_content(content) == result


def test_validate_content_blank():
    with pytest.raises(ValidationError):
        validate_content("   ")


def test_validate_content_too_long():
    with pytest.raises(ValidationError):
        validate_content("a" * 1001)


def test_validate_email():
    assert validate_email(" m1sharu@yandex.ru ") == "m1sharu@yandex.ru"
    assert validate_email("m1sharu@yandex.ru") == "m1sharu@yandex.ru"


def test_validate_email_blank():
    with pytest.raises(ValidationError):
        validate_email("   ")


def test_validate_email_invalid():
    with pytest.raises(ValidationError):
        validate_email(" jopasiski.ru")
