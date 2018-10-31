"""
Given an array of numbers, find the maximum sum of any contiguous subarray of
the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137,
since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not
take any elements.

Do this in O(N) time.
"""
from typing import List

def max_sub(arr: List[int]) -> int:
    max_so_far = max_sub = arr[0]
    for val in arr[1:]:
        max_so_far = max(val, max_so_far + val)
        max_sub = max(max_sub, max_so_far)
        print(f"max_so_far: {max_so_far}")
        print(f"max_sub: {max_sub}")
    return max_sub

def test_max_sub():
    assert max_sub([34, -50, 42, 14, -5, 86]) == 137
    assert max_sub([-5, -1, -8, -9]) == -1
