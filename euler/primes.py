"""Sieve of Eratosthenes"""
from functools import reduce
from collections import deque, Counter


def sieve(ceil=1000):
    """Prime number generator."""
    mods = deque([2, 3, 5, 7])
    arr = [True for i in range(ceil)]
    # Zero and One are not prime
    arr[0] = False
    arr[1] = False
    while mods:
        mod = mods.popleft()
        for n in range(0, ceil, mod):
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

def main():
    # # Project Euler #7
    # foo = sieve(1000000)
    # for i in range(10001):
    #     num = next(foo)
    # print(num)
    
    # Project Euler #10
    # prime_sum = sum([p for p in sieve(int(2e6))])
    # print(prime_sum)

    # Project Euler #12
    num_divs = 0
    target = 500
    triangle = lambda n: n * (n + 1) >> 1
    while num_divs < 500:
        num = triangle(target)
        divs = get_prime_factors(num)
        num_divs = reduce(lambda x, y: x * y, [i[1] + 1 for i in divs.items()])
        print(f"num: {num}, target: {target}, num_divs: {num_divs}")
        target += 1

if __name__ == "__main__":
    main()