"""
Fuel Injection Perfection
=========================

Commander Lambda has asked for your help to refine the automatic quantum antimatter fuel injection system for her LAMBCHOP doomsday device. It's a great chance for you to get a closer look at the LAMBCHOP - and maybe sneak in a bit of sabotage while you're at it - so you took the job gladly.

Quantum antimatter fuel comes in small pellets, which is convenient since the many moving parts of the LAMBCHOP each need to be fed fuel one pellet at a time. However, minions dump pellets in bulk into the fuel intake. You need to figure out the most efficient way to sort and shift the pellets down to a single pellet at a time.

The fuel control mechanisms have three operations:

1) Add one fuel pellet
2) Remove one fuel pellet
3) Divide the entire group of fuel pellets by 2 (due to the destructive energy released when a quantum antimatter pellet is cut in half, the safety controls will only allow this to happen if there is an even number of pellets)

Write a function called answer(n) which takes a positive integer as a string and returns the minimum number of operations needed to transform the number of pellets to 1. The fuel intake control panel can only display a number up to 309 digits long, so there won't ever be more pellets than you can express in that many digits.

For example:
answer(4) returns 2: 4 -> 2 -> 1
answer(15) returns 5: 15 -> 16 -> 8 -> 4 -> 2 -> 1


Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (string) n = "4"
Output:
    (int) 2

Inputs:
    (string) n = "15"
Output:
    (int) 5
"""

import pytest

# def answer(n):
#     int_n = int(n)
#     nearest_sq = 2**(int_n.bit_length() - 1)
#     diff = abs(int_n - nearest_sq)
#     if diff > nearest_sq // 2:
#         nearest_sq *= 2
#     return abs(nearest_sq - int_n) + nearest_sq.bit_length() - 1

def trail_zeros(num):
    z = 0
    num, rem = divmod(num, 2)
    while rem == 0 and num != 1:
        z += 1
        num, rem = divmod(num, 2)
    if num == 1 and rem == 0:
        z += 1
    return z

def answer(n):
    count = 0
    current = int(n)
    while True:
        zeros = trail_zeros(current)
        count += zeros
        current //= 2**zeros
        if current == 1:
            return count
        if current == 3: # corner case pow of 2
            return count + 2
        high = current + 1
        low = current - 1
        count += 1
        if trail_zeros(low) < trail_zeros(high):
            current = high
        else:
            current = low

test_list = [
    ("2", 1),
    ("3", 2),
    ("4", 2),
    ("15", 5),
    ("16", 4),
    ("30", 6),
    ("25", 6),
    ("24", 5),
    ("256", 8),
    ("258", 9),
]

@pytest.mark.parametrize("val, exp", test_list)
def test_answer(val, exp):
    assert answer(val) == exp
