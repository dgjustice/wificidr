"""
Given an array of integers, find the first missing positive integer in linear time 
and constant space. In other words, find the lowest positive integer that does not 
exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""

def find_missing(arr):
    low = 1
    if not arr:
        return low
    l = len(arr)
    for idx, val in enumerate(arr):
        t = 0
        if val <= l and val > 0:
            t = arr[val - 1]
            arr[val - 1] = val
            arr[idx] = t
        if t == low:
            low += 1
    return low

def test_find_missing():
    assert find_missing([3, 4, -1, 1]) == 2
    assert find_missing([1, 2, 0]) == 3
    assert find_missing([-1, -2, -4]) == 1
    assert find_missing([]) == 1
    assert find_missing([0]) == 1
    assert find_missing([9]) == 1
