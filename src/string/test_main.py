import pytest

from .main import is_substring
from .main import manacher


# ---------------------------
# Substring


def test_substring_positive_normal():
    assert is_substring("hello", "hello world!")
    assert is_substring("123", "1223")
    assert is_substring("123", "___1__2__3")


def test_substring_positive_empty():
    assert is_substring("", "hello")
    assert is_substring("", "")
    assert is_substring("", "")


def test_substring_positive_arr():
    assert is_substring([""], [""])
    assert is_substring(["hello"], ["hello", "world"])
    assert is_substring([[["hello"]]], [[["hello"]]])


def test_substring_tuple():
    assert is_substring((1, 2), (1, 2, 3))


def test_substring_tuple():
    assert is_substring((1, 2), (1, 2, 3))


def test_substring_egative_normal():
    # Case sensitive
    assert not is_substring("hello", "Hello world!")

    assert not is_substring("hello", "hell")
    assert not is_substring("hello", "ello")
    assert not is_substring("hello", "helo")


def test_substring_egative_types():
    with pytest.raises(TypeError):
        assert is_substring(None, None)

    with pytest.raises(TypeError):
        assert is_substring(1, 1)
