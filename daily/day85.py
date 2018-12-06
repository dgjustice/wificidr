def xyb(x: int, y: int, b: int) -> int:
    return x * (b & 1) + y * (b ^ 1)

def test_xyb_0():
    assert xyb(3, 10, 1) == 3

def test_xyb_1():
    assert xyb(3, 10, 0) == 10
