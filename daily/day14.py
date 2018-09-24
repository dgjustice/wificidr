from random import random
from math import sqrt, pi

NMAX = 30000
POINTS = [(random(), random()) for _ in range(NMAX)]

def dist(x1, y1, x2=0, y2=0):
    return sqrt((x2 - x1)**2 + (y2-y1)**2)

def gen_pi():
    in_ = 0
    out = 0
    for p in POINTS:
        if dist(p[0], p[1]) < 1.0: in_ += 1
        else: out += 1
    print("in", in_, "out", out)
    mypi = in_ / NMAX * 4
    print(f"mypi: {mypi}")
    p_diff = abs(pi - mypi) / pi
    print(f"percent diff: {p_diff}")
    return mypi

def test_dist():
    assert dist(0, 1) == 1.0
    assert dist(1, 0) == 1.0
    assert dist(3, 4) == 5.0

def test_gen_pi():
    assert abs(pi - gen_pi()) < 0.01

if __name__ == "__main__":
    gen_pi()
