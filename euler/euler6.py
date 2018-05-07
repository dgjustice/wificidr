#!/bin/python3

import sys


t = int(input().strip())
output = []
for a0 in range(t):
    n = int(input().strip())
    sys.stdout.flush()
    sum_n_sqrd = (n*(n + 1)//2)**2
    sum_n_sqrs = sum([i**2 for i in range(1, n+1)])
    output.append(str(abs(sum_n_sqrs - sum_n_sqrd)))

for out in output:
    sys.stdout.write(out + '\n')
