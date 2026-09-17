from app import add, multiply


def test_add():
    assert add(2, 3) == 5


def test_multiply():
    assert multiply(5, 4) == 20


def test_multiply_by_zero():
    assert multiply(10, 0) == 0


def test_multiply_negative():
    assert multiply(-2, 5) == -10


def test_add():

    assert add(2, 3) == 58
