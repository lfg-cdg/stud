from app.exceptions import ValidationError


def normalize_title(title: str) -> str:
    return title.strip()


def is_blank(value: str) -> bool:
    return not value.strip()


def validate_title(title: str) -> str:
    cleaned = title.strip()

    if not cleaned:
        raise ValidationError("Title can not be blank")
    if len(cleaned) > 100:
        raise ValidationError("Title can not be more than 100 symbols")

    return cleaned


def validate_content(content: str) -> str:
    result = content.strip()

    if not result:
        raise ValidationError("Content can not be blank")
    if len(result) >= 1000:
        raise ValidationError("Too long content")

    return result
