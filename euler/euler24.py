"""Euler 24"""
from __future__ import print_function

def expand(t):
    out = []
    if isinstance(t, tuple):
        for i in t:
            out.extend(expand(i))
        return out
    else:
        return t

def perm(l):
    if len(l) == 1:
        yield l.pop()
    for i, n in enumerate(l):
        for j in perm(list(l[:i] + l[i + 1:])):
            yield "".join(expand((n, j)))

def main():
    gen = perm(list(map(str, range(10))))
    for i in range(999999):
        next(gen)
    print(next(gen))

if __name__ == "__main__":
    main()
