"""
This is the calculator test file
"""

from calculator import add, sum, div


# this is an example
def test_add():
    assert add(0, 0) == 0, "result not correct"
    assert add(1, 2) == 3, "result not correct"


# add your tests here
def test_sum():
    assert sum(1, 2) == 3
    assert sum(1, 3, 7, 3) == 14
    assert sum(*[1, 2, -3]) == 0


def test_div():
    assert div(1, 1) == 1
    assert div(3, 3) == 1
    assert div(2, 8) == 0.25