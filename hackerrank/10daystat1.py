import sys

test_input = """9
3 7 8 5 12 14 21 13 18"""

def split_median(nums):
    # Compute median and return upper/lower halves
    mid = len(nums) // 2
    if len(nums) % 2 == 0:
        lower = nums[0:mid]
        upper = nums[mid:]
        x = sum(nums[mid - 1: mid + 1]) / 2
    else:
        lower = nums[0:mid]
        upper = nums[mid + 1:]
        x = nums[mid]
    return x, lower, upper


def main(num_len, nums):
    num_len = int(num_len)
    nums = sorted([int(i) for i in nums.split()])
    x, l, u = split_median(nums)
    lx, _, _ = split_median(l)
    ux, _, _ = split_median(u)
    print(int(lx))
    print(int(x))
    print(int(ux))

if __name__ == "__main__":
    num_len = next(sys.stdin)
    nums = next(sys.stdin)
    main(num_len, nums)
else:
    # python3 -m xxx.py
    main(*test_input.split("\n"))