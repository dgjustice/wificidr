"""
Given an array of time intervals (start, end) for classroom lectures (possibly 
overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""
from typing import List, Tuple
from heapq import heappop, heappush

def rooms(sched: List[Tuple[int, int]]) -> int:
    heads: List[int] = []
    tails: List[int] = []
    for slot in sched:
        heappush(heads, slot[0])
        heappush(tails, slot[1])
    rooms = []
    max_rooms = 0
    while heads:
        current = heappop(heads)
        if current < tails[0]:
            rooms.append(current)
            room_len = len(rooms)
            if max_rooms < room_len:
                max_rooms = room_len
        else:
            while current >= tails[0]:
                heappop(tails)
    return max_rooms


def test_rooms():
    assert rooms([(30, 75), (0, 50), (60, 150)]) == 2
    assert rooms([(30, 75), (20, 40), (0, 50), (60, 150)]) == 3
    assert rooms([(30, 75), (20, 40), (20, 40), (0, 50), (60, 150)]) == 4
    assert rooms([(30, 75), (80, 150)]) == 1
    assert rooms([(30, 75), (75, 150)]) == 1
