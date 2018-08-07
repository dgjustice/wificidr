import math
import sys
import time

# Problem 1
sum3or5 = sum(filter(lambda x: (x % 3 == 0 or x % 5 == 0), range(1000)))
print("Problem 1: %d" % sum3or5)

# Problem 2
def fibonacci(seed, cb):
    low = seed[0]
    high = seed[1]
    while not cb(low + high):
        fib = low + high
        yield fib
        low = high
        high = fib

def cb(limit):
    return True if limit >= 4000000 else False

print("Problem 2: %d" % sum(filter(
    lambda x: x % 2 ==0, [i for i in fibonacci((0, 1), cb)])))

"""
Problem 3:
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
num = 600851475143

for i in range(3, int(math.floor(float(num)/2)), 2):
    if num % i == 0:
        print(i)

"""
Problem 16
sum of the digits of 2^1000
"""
foo = sum([int(i) for i in str(2**1000)])
