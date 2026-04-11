from app.utils import is_blank, normalize_title


def test_normalize_title_strip_spaces():
    res = normalize_title("   jope  ")

    assert res == "jope"

def test_is_value_blank():
    res1 = is_blank("jopa")
    res2 = is_blank("   ")
    res3 = is_blank("")

    assert not res1
    assert res2 
    assert res3 
