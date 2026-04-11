def normalize_title(title: str) -> str:
    return title.strip()


def is_blank(value: str) -> bool:
    return not value.strip()
