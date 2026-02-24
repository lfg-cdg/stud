def is_same_object(a, b) -> bool:
    return a is b


def is_equal(a, b) -> bool:
    return a == b


def relation(a, b) -> str:
    if a is b:
        return "same object"
    if a == b:
        return "equal"

    return "different"
