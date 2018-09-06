"""Sieve of Eratosthenes"""
from functools import reduce
from collections import deque, Counter, defaultdict
from math import sqrt, floor, ceil


def sieve(ceiling=1000):
    """Prime number generator."""
    mods = deque([2, 3, 5, 7])
    arr = [True for i in range(ceiling)]
    # Zero and One are not prime
    arr[0] = False
    arr[1] = False
    while mods:
        mod = mods.popleft()
        for n in range(0, ceiling, mod):
            if n <= mod:
                continue
            if not n % mod:
                arr[n] = False
        yield mod
        if not mods:
            try:
                mods.append(arr.index(True, mod + 1))
            except ValueError:
                return

def get_prime_factors(num):
    """Calculate prime factorization of a number."""
    out = num
    factors = []
    # if n is even
    if num & 1 == 0:
        while num > 1:
            if num & 1 == 0:
                num //= 2   
                factors.append(2)
            else:
                break
        if num == 1:
            return Counter(factors)
    i = 3
    while i**2 < num:
        if num % i == 0:
            factors.append(i)
            num //= i
            i = 1
        i += 2
    if num > 2:
        factors.append(num)
    return Counter(factors)

def memoize(func):
    """Function memoizer."""
    mem = {}
    def wrapper(num):
        if num not in mem:
            mem[num] = func(num)
        return mem[num]
    return wrapper

@memoize
def get_divisors(num):
    """Return set of integral divisors of num."""
    if num < 1:
        raise ValueError("num must be > 0")
    divs = {1}
    for i in range(2, floor(sqrt(num)) + 1):
        if not (num % i):
            divs.add(i)
            divs.add(num // i)
    return divs
    
def amicable(max_num):
    """Find amicable numbers <= max_num"""
    am = set()
    for num in range(1, max_num + 1):
        divs = sum(get_divisors(num))
        if divs > 1:
            a_divs = sum(get_divisors(divs))
            if num == a_divs and a_divs != divs:
                am.update({num, a_divs})
    print(sum(am))

def main():
    # # Project Euler #7
    # foo = sieve(1000000)
    # for i in range(10001):
    #     num = next(foo)
    # print(num)
    
    # Project Euler #10
    # prime_sum = sum([p for p in sieve(int(2e6))])
    # print(prime_sum)

    # # Project Euler #12
    # num_divs = 0
    # target = 500
    # triangle = lambda n: n * (n + 1) >> 1
    # while num_divs < 500:
    #     num = triangle(target)
    #     divs = get_prime_factors(num)
    #     num_divs = reduce(lambda x, y: x * y, [i[1] + 1 for i in divs.items()])
    #     print(f"num: {num}, target: {target}, num_divs: {num_divs}")
    #     target += 1

    # # Euler #23
    # ceiling = 28123
    # abund = set()
    # out = 0
    # for i in range(1, ceiling):
    #     divs = get_divisors(i)
    #     sig = sum(divs)
    #     if sig > i:
    #         abund.add(i)
    #     if not any([(i - a) in abund for a in abund]):
    #         out += i
    # print(out)
    # amicable(10000)
    pass

if __name__ == "__main__":
    main()
