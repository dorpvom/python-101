import pytest
from calculator import add, div, sub

def test_add():
    assert sum(range(10)) == add(range(10))

def test_div():
    with pytest.raises(ValueError):
        div(10, 0)
    assert div(10, 2) == 5


def test_sub():
    assert sub(1, 2) == -1
