from functools import reduce
reduce_not_one = lambda n: reduce(lambda x, y: x * y, range(1, n + 1))
prod = lambda n: 1 if n == 1 else reduce_not_one(n)
comb = lambda n, k: 1 if not n - k else prod(n) / (prod(n - k) * prod(k))
p = 1.09 / 2.09
q = 1 - p
print("{:.3f}".format(round(sum([comb(6, i)*(p**i)*(q**(6 - i)) for i in [3, 4, 5, 6]]), 3)))
