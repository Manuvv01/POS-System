import pytest

def add_num(num1, num2):
    return num1+num2

def test_add_num():
    assert add_num(2,3) == 5