import pytest
from src.session_06.exercise_challenge.main import factorial

def test_factorial_positive():
    assert factorial(5) == 120  # 5! = 5 * 4 * 3 * 2 * 1 = 120

def test_factorial_zero():
    assert factorial(0) == 1  # 0! = 1 by definition

def test_factorial_negative():
    with pytest.raises(ValueError, match="Factorial is not defined for negative numbers."):
        factorial(-5)  # Should raise an exception

def test_factorial_one():
    assert factorial(1) == 1  # 1! = 1

def test_factorial_large_number():
    assert factorial(10) == 3628800  # 10! = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 = 3,628,800