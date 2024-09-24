import pytest

from StringUtils import StringUtils

SU = StringUtils()


@pytest.mark.parametrize(
        "word, result", [("skydabbler", "Skydabbler"), ("Sky", "Sky")])
def test_SU_positive(word, result):
    SU = StringUtils()
    res = SU.capitilize(word)
    assert res == result


@pytest.mark.parametrize(
    "word, result", [("  123", "123"), ("123", "123"), ("       ", "")]
)
def test1_positive(word, result):
    SU = StringUtils()
    res = SU.trim(word)
    assert res == result


def test2_positive():
    SU = StringUtils()
    res = SU.to_list("a,b,c,d")
    assert res == ["a", "b", "c", "d"]


@pytest.mark.parametrize("word, result", [("d", True), ("U", False)])
def test3_positive(word, result):
    SU = StringUtils()
    res = SU.contains("dabbler", word)
    assert res == result


@pytest.mark.parametrize("word, symbol, result", [("dabbler", "b", "daler")])
def test4_positive(word, symbol, result):
    SU = StringUtils()
    res = SU.delete_symbol(word, symbol)
    assert res == result


@pytest.mark.parametrize(
    "word, symbol, result", [("result", "r", True), ("result", "s", False)]
)
def test5_positive(word, symbol, result):
    SU = StringUtils()
    res = SU.starts_with(word, symbol)
    assert res == result


@pytest.mark.parametrize(
    "word, symbol, result", [("SkyPro", "o", True), ("SkyPro", "y", False)]
)
def test6_positive(word, symbol, result):
    SU = StringUtils()
    res = SU.end_with(word, symbol)
    assert res == result


@pytest.mark.parametrize(
        "word, result", [("SkyPro", False), ("", True), (" ", True)])
def test7_positive(word, result):
    SU = StringUtils()
    res = SU.is_empty(word)
    assert res == result


@pytest.mark.parametrize(
    "word, result", [(["Sky", "Pro"], "Sky, Pro"), ([1, 2, 3, 4], "1, 2, 3, 4")
                     ]
)
def test8_positive(word, result):
    SU = StringUtils()
    res = SU.list_to_string(word)
    assert res == result


def test9_positive():
    SU = StringUtils()
    res = SU.list_to_string(["Sky", "Pro"], "-")
    assert res == "Sky-Pro"


def test_SU_negative():
    SU = StringUtils()
    res = SU.capitilize("1kydabbler")
    assert res == "1kydabbler"


@pytest.mark.parametrize(
        "word, result", [("1 2 3", "1 2 3"), ("123   ", "123   ")])
def test1_negative(word, result):
    SU = StringUtils()
    res = SU.trim(word)
    assert res == result


@pytest.mark.parametrize("string, result", [
    ("", []),
    ("1,2,3", ["1", "2", "3"]),
    ("     ", ["     "])
])
def test2_negative(string, result):
    SU = StringUtils()
    assert SU.to_list(string) == result


@pytest.mark.parametrize("word, result", [("", False), ("d", True)])
def test3_negative(word, result):
    SU = StringUtils()
    assert SU.contains("dabbler", word) == result


@pytest.mark.parametrize(
    "word, symbol, result", [
     (" result", "r", False),
     ("result", "r", True),
     ("result", "♣☺♂", False)])
def test5_negative(word, symbol, result):
    SU = StringUtils()
    assert SU.starts_with(word, symbol) == result


def test9_negative():
    SU = StringUtils()
    with pytest.raises(AssertionError):
        res = SU.list_to_string(["Sky", "Pro"], "")
        assert res == "Sky, Pro"


def test_contains_with_none():
    assert SU.contains(None, 'a') is False


def test_delete_symbol_with_none():
    assert SU.delete_symbol(None, 'a') is None


def test_starts_with_none():
    assert SU.starts_with(None, 'a') is False


def test_end_with_none():
    assert SU.end_with(None, 'o') is False


def test_trim_with_spaces():
    assert SU.trim("   hello   ") == "hello   "
    assert SU.trim("   ") == ""


def test_capitalize_with_spaces():
    assert SU.capitilize(" hello ") == "Hello "


def test_delete_symbol_with_spaces():
    assert SU.delete_symbol("   hello   ", " ") == "hello"
