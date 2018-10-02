"""
Given an array of integers and a number k, where 1 <= k <= length of the array, 
compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)
Do this in O(n) time and O(k) space. You can modify the input array in-place and you 
do not need to store the results. You can simply print them out as you compute them.
"""
from heapq import heappush, heappop

def my_func(arr, k):
    if len(arr) <= k:
        return max(arr)
    h = []
    max_vals = []
    for idx, val in enumerate(arr):
        heappush(h, (-1 * val, idx))
        if idx < k - 1: continue
        while h and h[0][1]  < idx - k + 1:
            heappop(h)
        max_vals.append(h[0][0] * -1)
    return max_vals


def test_it():
    assert my_func([10, 5, 2, 7, 8, 7], 3) == [10, 7, 8, 8]
    assert my_func([-1, 3, 9, 22, 10, 5, 2, 7, 8, 7], 3) == [9, 22, 22, 22, 10, 7, 8, 8]

print(my_func([10, 5, 2, 7, 8, 7], 3))
