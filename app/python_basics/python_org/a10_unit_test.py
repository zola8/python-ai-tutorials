import pytest

from a10_functions import eat, inc, error


def test_answer():
    assert inc(4) == 5


def test_apple():
    assert eat() == 'eaten'


def test_answer_error():
    with pytest.raises(ValueError):
        error()
