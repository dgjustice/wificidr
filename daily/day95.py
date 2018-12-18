"""Calculate lexicographical permutations of an ordered sequence."""
from functools import reduce

def permute(l, pre=[]):
    """Find all the perms."""
    for i in l:
        tmp = list(l)
        tmp.remove(i)
        if not tmp: yield pre + l
        yield from permute(tmp, pre + [i])

def test_permute():
    """Testing against know answer to millionth base-10 perm."""
    foo = list(range(10))
    g = permute(foo)
    for _ in range(999999):
        next(g)
    assert reduce(
        lambda x, y: x + y, map(
            lambda t: 10**t[0] * t[1], enumerate(next(g)[::-1])
        )
    ) == 2783915460
