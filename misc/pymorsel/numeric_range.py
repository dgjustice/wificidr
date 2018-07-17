"""Numeric range challenge from Python Morsel trial."""
from typing import Iterable

def numeric_range(iterable: Iterable) -> int:
    """Return the difference between the highest and lowest element."""
    pos = -1
    for pos, item in enumerate(iterable):
        # Have to define low and high if this is the first pass
        if pos:
            if item < low:
                low = item
            if item > high:
                high = item
        else:
            low = item
            high = item
    if pos != -1:
        return high - low
    return 0
