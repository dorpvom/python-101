"""
This is the calculator test file
"""

from calculator import add, summation, div

# this is an example
def test_add():
    assert add(0, 0) == 0, "result not correct"
    assert add(1, 2) == 3, "result not correct"


# add your tests here
def test_summation():
    assert summation(list(range(10))) == 45, "result not correct"
    assert summation([-2, 5, 15, -60, 0]) == -42, "result not correct"

def test_div():
    assert div(20, 5) == 4, "result not correct"
    assert div(1, 2) == 0.5, "result not correct"