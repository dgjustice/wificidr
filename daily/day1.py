# True if sum(2 vals) == k
# [10, 15, 3, 7] and k of 17, return True

from random import choices
from hypothesis import given, strategies as st

def find_it(vals, k):
    opts = set()
    for val in vals:
        opt = k - val
        if val in opts:
            return True
        opts.add(opt)
    return False

@given(st.lists(st.integers()))
def test_find_it(xs):
    v1, v2 = (0, 0)
    if len(xs) > 1:
        t = list(xs)
        v1 = choices(t)[0]
        t.remove(v1)
        v2 = choices(t)[0]

    k = v1 + v2
    if len(xs) > 1:
        assert find_it(xs, k)
    else:
        assert not find_it(xs, k)

if __name__ == "__main__":
    vals = [10, 15, 3, 7]
    k = 17

    print(find_it(vals, k))
