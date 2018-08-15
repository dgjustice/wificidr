#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 13:02:28 2018

@author: d0j00jm
"""

import math
import networkx as nx

def dijkstra(source, graph):
    """Compute shortest paths."""
    # TODO: This should be a heap
    dist = {node: "infinity" for node in graph.nodes}
    num_vertices = len(graph.nodes)
    dist[source] = 0
    spt_set = set()
    spt = dict()
    vertex = source
    while len(spt_set) < num_vertices:
        spt_set.add(vertex)
        for neigh in graph.neighbors(vertex):
            if neigh not in spt_set:
                alt = graph.edges[(vertex, neigh)]["weight"] + dist[vertex]
                if dist[neigh] == "infinity" or alt < dist[neigh]:
                    dist[neigh] = alt
                    spt[neigh] = vertex
        diff = [
            (ver, dist[ver]) for ver in set(dist.keys()) - spt_set if dist[ver] != "infinity"
        ]
        if diff:
            node = min(
                diff, key=lambda x: x[1]
            )
            vertex = node[0]
        elif len(spt_set) < num_vertices:
            # There are unreachable vertices, sanity break
            break
    return dist, spt

graph = [
    (0, 1, {"weight": 4}),
    (0, 7, {"weight" : 8}),
    (1, 7, {"weight" : 11}),
    (1, 2, {"weight" : 8}),
    (7, 8, {"weight" : 7}),
    (7, 6, {"weight" : 1}),
    (2, 8, {"weight" : 2}),
    (8, 6, {"weight" : 6}),
    (5, 6, {"weight" : 2}),
    (2, 5, {"weight" : 4}),
    (3, 2, {"weight" : 7}),
    (3, 5, {"weight" : 14}),
    (3, 4, {"weight" : 9}),
    (5, 4, {"weight" : 10}),
    # Unreachable for sanity check
    (9, 10, {"weight": 3}),
]

G = nx.Graph()
G.add_edges_from(graph)
nx.draw(G, with_labels=True, font_weight='bold')