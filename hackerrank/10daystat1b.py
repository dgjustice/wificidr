import sys

test_input = """6
6 12 8 10 20 16
5 4 3 2 1 5"""

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


def main(num_len, nums, freqs):
    num_len = int(num_len)
    nums = [int(i) for i in nums.split()]
    freqs = [int(i) for i in freqs.split()]
    assert len(nums) == len(freqs)
    nums = sorted([j for i in map(lambda x: [x[0]] * x[1], zip(nums, freqs)) for j in i])

    _, l, u = split_median(nums)
    lx, _, _ = split_median(l)
    ux, _, _ = split_median(u)
    print("{0:.1f}".format(ux -lx))

if __name__ == "__main__":
    num_len = next(sys.stdin)
    nums = next(sys.stdin)
    freqs = next(sys.stdin)
    main(num_len, nums, freqs)
else:
    # python3 -m xxx.py
    main(*test_input.split("\n"))