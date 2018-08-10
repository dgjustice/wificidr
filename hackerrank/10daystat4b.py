from functools import reduce
reduce_not_one = lambda n: reduce(lambda x, y: x * y, range(1, n + 1))
prod = lambda n: 1 if n in [0, 1] else reduce_not_one(n)
comb = lambda n, k: 1 if not n - k else prod(n) / (prod(n - k) * prod(k))

p = 0.12
q = 1 - p

n = 10

print("{:.3f}".format(round(sum([comb(n, x) * (p**x) * (q**(n - x)) for x in [0, 1, 2]]), 3)))

print("{:.3f}".format(round(sum([comb(n, x) * (p**x) * (q**(n - x)) for x in range(2, 11)]), 3)))