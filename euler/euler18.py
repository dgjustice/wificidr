# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math
from collections import defaultdict
import networkx as nx

def load_triangle_graph(fname):
    """Load triangle graph from fname."""
    with open(fname) as fp:
        nums = list(map(int, fp.read().split()))
    # binomial expansion of n^2 + n
    n = int(math.sqrt(len(nums) * 2 + 1/4) - 1/2)
    other = defaultdict(list)
    dist = {idx: w for idx, w in enumerate(nums)}
    for i in range(n - 1):
        base = i * (i + 1) // 2
        for j in range(i + 1):
            a = base + j + i + 1
            b = base + j + i + 2
            v = base + j
            other[a].append(v)
            other[b].append(v)
    for idx, weight in enumerate(nums):
        parents = other.get(idx)
        if parents:
            dist[idx] += max([dist[p] for p in parents])
            # print(f"{idx}->{parents}")
    # Euler 67
    print(max([dist[i] for i in range(4950, 5050)]))

G = nx.Graph()
load_triangle_graph("triangle.txt")
