#!/bin/python3

import sys

def gcf(num1, num2):
    high = max(num1, num2)
    low = min(num1, num2)
    res = high
    c = 1
    while res > low:
        res -= low
        if res < low:
            tmp = res
            res = low
            low = tmp
        c += 1
    return res

def func(target):
    num = 1
    for i in range(1, target + 1):
        res = gcf(num, i)
        if res == 1:
            num *= i
        else:
            mul = min(num, i) // res
            num *= mul
    print(num)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    if n == 1:
        sys.stdout.flush()
        print(n)
        continue
    func(n)
