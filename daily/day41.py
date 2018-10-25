"""
Given an unordered list of flights taken by someone, each represented as (origin, 
destination) pairs, and a starting airport, compute the person's itinerary. If no 
such itinerary exists, return null. If there are multiple possible itineraries, 
return the lexicographically smallest one. All flights must be used in the itinerary.

For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), 
('HKO', 'ORD')] and starting airport 'YUL', you should return the list 
['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 
'COM', you should return null.

Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and 
starting airport 'A', you should return the list ['A', 'B', 'C', 'A', 'C'] even 
though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary. However, the first 
one is lexicographically smaller.
"""
from typing import List, Tuple, Dict, Any, Optional
from collections import defaultdict
from heapq import heappush, heappop

def itenerary(flights: List[Tuple[str, str]], start: str) -> Optional[List[str]]:
    # build a hash so we're not constantly scanning the flights list
    segs: Dict = defaultdict(list)
    # heap preserves lexicographical property
    for seg in flights:
        heappush(segs[seg[0]], seg[1])
    if start not in segs:
        return None
    path = [start]
    while True:
        if segs[start]:
            hop = heappop(segs[start])
        else: # no next hop
            break
        path.append(hop)
        start = hop
    leftovers: List[Any] = []
    for k, v in segs.items():
        leftovers.extend(v)
    if leftovers:
        return None
    return path

def test_itenerary():
    assert itenerary([
        ('SFO', 'HKO'),
        ('YYZ', 'SFO'),
        ('YUL', 'YYZ'),
        ('HKO', 'ORD')
    ], "YUL") == ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']

def test_itenerary2():
    assert itenerary([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')], "A") == [
        'A', 'B', 'C', 'A', 'C'
    ]

def test_itenerary3():
    assert itenerary([
        ('SFO', 'HKO'),
        ('YUL', 'YYZ'),
        ('HKO', 'ORD')
    ], "YUL") == None
    assert itenerary([
        ('SFO', 'HKO'),
        ('YYZ', 'SFO'),
        ('YUL', 'YYZ'),
        ('HKO', 'ORD')
    ], "ABC") == None
