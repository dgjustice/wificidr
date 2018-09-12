from functools import reduce

"""
Given an array of integers, return a new array such that each element at index i 
of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
If our input was [3, 2, 1], the expected output would be [2, 3, 6].
"""

def prodder(in_list):
    """Return the product of elems in the list except for the current elem."""
    return [reduce(lambda x, y: x * y, elems) for elems in [
        in_list[:i - 1] + in_list[i:] for i, _ in enumerate(in_list, 1)
    ]]

def test_prodder():
    assert prodder([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
    assert prodder([3, 2, 1]) == [2, 3, 6]

