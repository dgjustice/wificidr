import pytest
from hypothesis import given
from hypothesis.strategies import integers

def div_nodiv(a: int, b: int) -> int:
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    i = 0
    q = abs(a)
    while q >= abs(b):
        i += 1
        q -= abs(b)
    if (a < 0) ^ (b < 0):
        i *= -1
    return i

def test_divnodiv():
    assert div_nodiv(12, 4) == 3
    assert div_nodiv(4, 12) == 0
    assert div_nodiv(0, 1) == 0
    assert div_nodiv(-12, 4) == -3
    assert div_nodiv(-12, -4) == 3
    assert div_nodiv(-4, 3) == -1
    with pytest.raises(ValueError):
        div_nodiv(0, 0)
    with pytest.raises(ValueError):
        div_nodiv(234, 0)
    with pytest.raises(ValueError):
        div_nodiv(-24, 0)

@given(x=integers(min_value=-10000), y=integers(max_value=10000))
def test_hypothesis(x, y):
    # Ignore 0 for this test
    if y == 0:
        y += 1
    # Can't use // because python floor divides
    assert div_nodiv(x, y) == int(float(x)/y)
