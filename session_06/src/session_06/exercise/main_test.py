from session_06.src.session_06.exercise.main import multiply

def test_multiply_integers():
    assert multiply(2, 3) == 6

def test_multiply_floats():
    assert multiply(2.5, 4) == 10.0

def test_multiply_negative_numbers():
    assert multiply(-2, 3) == -6
    assert multiply(2, -3) == -6

def test_multiply_zero():
    assert multiply(0, 5) == 0
    assert multiply(5, 0) == 0

def test_multiply_mixed_types():
    assert multiply(2, 3.5) == 7.0
    assert multiply(2.5, 3) == 7.5