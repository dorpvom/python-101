'''
Clean Code 101 calculator hands on

Task 0: Create a branch and switch to it

Task 1: Add and test a "devide(a, b)" (a/b) function
Hints:
- consider the b = 0 case!
- add your tests to src/tests/test_calculator.py

Task 2: Add and test a "sum(LIST)" function that adds all items in the list
Hints:
- LIST shall have arbitrary many items
- consider the len(LIST) = 0 case!
- add your tests to src/tests/test_calculator.py

Task 3.1: Push your branch to the remote repository
Task 3.2: Setup a Merge Request and assign it to your supervisor
'''
from typing import Iterable, Union


# this is an example
# def add(a, b):
#     return a+b

def add(summands: Iterable[Union[float, int]]) -> Union[float, int]:
    return sum(summands)

def div(divident: Union[float, int], divisor: Union[float, int]) -> Union[int, float]:
    if divisor == 0:
        raise ValueError
    return divident / divisor

def sub(a, b):
    return a - b

