import sys, operator
from collections import defaultdict
from functools import reduce
test_input = """5
10 40 30 50 20
1 2 3 4 5"""

def main(num_len, nums, weights):
    num_len = int(num_len)
    nums = [int(i) for i in nums.split()]
    weights = [int(i) for i in weights.split()]
    wmean = reduce(lambda x, y: x + y, map(operator.mul, nums, weights)) / sum(weights)

    print("{0:.1f}".format(wmean))

if __name__ == "__main__":
    num_len = next(sys.stdin)
    nums = next(sys.stdin)
    weights = next(sys.stdin)
    main(num_len, nums, weights)
else:
    # python3 -m xxx.py
    main(*test_input.split("\n"))
