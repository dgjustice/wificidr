from functools import reduce

def gen_pairs():
    """sum-10 pair generator."""
    counter = 0
    pairs = [(n, 10 - n) for n in range(1, 6)]
    while True:
        yield pairs[counter % 5]
        counter += 1

def perfect_():
    """Generator to return next num."""
    pair_gen = gen_pairs()
    idx = 0
    while True:
        zeros, rem = divmod(idx, 5)
        print(zeros, "idx", idx)
        for outer in range(5):
            pairs = next(pair_gen)
            for pos in range(zeros + 1):
                yield pairs[0] * 10**(zeros + 1) + pairs[1] * 10**pos
            idx += 1

def perfect(nth):
    """Return the nth number whose digits sum to 10."""
    perfect_gen = perfect_()
    for idx in range(nth):
        num = next(perfect_gen)
    return num

def test_perfect():
    """Test given test cases."""
    assert perfect(1) == 19
    assert perfect(2) == 28
    assert perfect(6) == 109
    assert perfect(7) == 190
    assert perfect(16) == 1009
