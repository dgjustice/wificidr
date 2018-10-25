"""
We can determine how "out of order" an array A is by counting the number of inversions 
it has. Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j. 
That is, a smaller element appears after a larger element.

Given an array, count the number of inversions it has. Do this faster than O(N^2) time.

You may assume each element in the array is distinct.

For example, a sorted list has zero inversions. The array [2, 4, 1, 3, 5] has 
three inversions: (2, 1), (4, 1), and (4, 3). The array [5, 4, 3, 2, 1] has ten 
inversions: every distinct pair forms an inversion.
"""
from typing import List

def inversions(input_list: List[int]) -> int:
    invs = 0
    c = 0
    for i in range(len(input_list)):
        for j in range(i + 1, len(input_list)):
            if input_list[i] > input_list[j]:
                invs += 1
            c += 1
    return invs

def test_inv():
    assert inversions([2, 4, 1, 3, 5]) == 3
    assert inversions([5, 4, 3, 2, 1]) == 10
    assert inversions(list(range(10))) == 0
    assert inversions([3] * 100) == 0
