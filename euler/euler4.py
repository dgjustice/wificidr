#!/bin/python3

import sys
import math

def factors(num):
    for i in range(999, 100, -1):
        if num % i == 0:
            yield i

t = int(input().strip())
nums = []
for a0 in range(t):
    nums.append(int(input().strip()))
sys.stdout.flush()

for num in nums:
    # Find the largest palindrome made from the product of two 3-digit numbers which is less than N
    # 999**2 = 998001
    if num > 998001:
        num = 998001
    for i in range(int(str(num)[:3]), 100, -1):
        numstr = str(i)
        pal = int(numstr + numstr[::-1])
        if pal < num:
            # get a list of factors
            facts = list(factors(pal))
            if facts:
                # factors have to be 3-digit multiples
                comps = list(filter(lambda x: pal // x < 1000, facts))
                if comps:
                    print(pal)
                    break
