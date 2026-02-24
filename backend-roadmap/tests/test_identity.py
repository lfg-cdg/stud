from src.foundation.identity import is_equal, is_same_object, relation


def test_same_lists():
    a = [1, 2, 3]
    b = [1, 2, 3]
    assert not is_same_object(a, b)
    assert is_equal(a, b)
    assert relation(a, b) == "equal"


def test_same_links():
    a = 123
    b = a

    assert is_same_object(a, b)
    assert is_equal(a, b)
    assert relation(a, b) == "same object"


def test_different_values():
    a = 123
    b = "asas"

    assert not is_same_object(a, b)
    assert not is_equal(a, b)
    assert relation(a, b) == "different"


def none_compare():
    a = None
    b = None

    assert is_same_object(a, b)
    assert is_equal(a, b)
    assert relation(a, b) == "same object"
