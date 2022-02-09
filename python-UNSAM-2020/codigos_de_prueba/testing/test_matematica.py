from matematica import *


def test_suma():
    assert suma(1, 2) == 3
    assert suma(-1, 5) == 4
    assert suma(0, 0) == 0
