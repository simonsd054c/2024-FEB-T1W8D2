import pytest
from calculator import add, subtract, division

def test_basic():
    assert "hello" == "hello"

def test_add():
    assert add(2, 3) == 5
    assert add(5, 7) == 12
    assert add(2, 0) == 2
    assert add(5, -7) == -2
    assert add(5, 2) != 6
    assert add(5, 1) >= 5

def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(-7, -5) == -2

def test_division():
    assert division(10, 2) == 5

def test_division_raise_error():
    with pytest.raises(Exception):
        division(2, 0)