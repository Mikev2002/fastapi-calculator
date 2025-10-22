# test_operations.py

from operations import add, subtract, multiply, divide
import pytest

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(10, 4) == 6

def test_multiply():
    assert multiply(3, 4) == 12

def test_divide():
    assert divide(8, 2) == 4

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)
