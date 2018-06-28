import sys
from collections import defaultdict
test_input = """10
64630 11735 14216 99233 14470 4978 73429 38120 51135 67060"""

def main(num_len, nums):
    # num_len, nums = test_input.split("\n")
    num_len = int(num_len)
    nums = sorted([int(i) for i in nums.split()])
    nums_dict = defaultdict(int)
    total = 0
    max_mode = (0, 1)
    for i in nums:
        total += i
        nums_dict[i] += 1
        if nums_dict[i] > max_mode[1]:
            max_mode = (i, nums_dict[i])
    if max_mode[1] == 1:
        mode = nums[0]
    else:
        mode = max_mode[0]

    mean = total / float(num_len)

    mid = num_len // 2
    if len(nums) % 2 == 0:
        median = (nums[mid - 1] + nums[mid]) / 2
    else:
        median = nums[mid + 1]

    print("{0:.1f}".format(mean))
    print("{0:.1f}".format(median))
    print("{}".format(mode))

if __name__ == "__main__":
    num_len = next(sys.stdin)
    nums = next(sys.stdin)
    main(num_len, nums)
