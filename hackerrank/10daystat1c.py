import sys
import math

test_input = """5
10 40 30 50 20"""

def main(num_len, nums):
    num_len = int(num_len)
    nums = sorted([int(i) for i in nums.split()])
    u = sum(nums) / num_len
    diffs = [(i - u)**2 for i in nums]
    s = math.sqrt(sum(diffs) / num_len)
    print("{0:.1f}".format(s))

if __name__ == "__main__":
    num_len = next(sys.stdin)
    nums = next(sys.stdin)
    main(num_len, nums)
else:
    # python3 -m xxx.py
    main(*test_input.split("\n"))