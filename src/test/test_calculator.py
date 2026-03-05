"""
This is the calculator test file
"""

from calculator import add, sum_over, divide
import pytest

# this is an example
def test_add():
    assert add(0, 0) == 0, "result not correct"
    assert add(1, 2) == 3, "result not correct"


# add your tests here
def test_sum_over():
    assert sum_over(1, 2, 3, 4) == 10, "result not correct"

def test_divide():
    assert divide(10, 2) == 5, "result not correct"
    assert divide(5, 1) == 5, "dividing by 1 should always result in the original number"
    with pytest.raises(ZeroDivisionError):
        divide(2, 0)