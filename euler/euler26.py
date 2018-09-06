"""Euler problem 26, repeating decimal fraction."""
from math import log, floor, ceil

log10 = lambda x: log(x, 10)

def divide(num):
    """Look for patterns in decimal fraction."""
    rem = 1
    mods = {1}
    while True:
        while rem < num:
            rem *= 10
        rem = rem % num
        if not rem:
            return 0
        if rem in mods:
            return len(mods)
        mods.add(rem)

def test_divide():
    """Test against known case"""
    assert divide(7) == 6
    assert divide(3) == 1

if __name__ == "__main__":
    print(max([(n, divide(n)) for n in range(1, 1001)], key=lambda x: x[1]))
