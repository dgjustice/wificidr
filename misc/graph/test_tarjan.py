#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import networkx as nx
from tarjan import tarjan
import pytest

def draw_network():
    """Draw a realistic NW graph."""
    g = nx.Graph()
    leaves = [f"leaf{x}" for x in range(1, 7)]
    spines = [f"spine{x}" for x in range(1, 5)]
    cores = [f"core{x}" for x in range(1, 5)]
    sums = [f"sum{x}" for x in range(1, 3)]
    dists = [f"dist{x}" for x in range(1, 7)]
    edges = [f"edge{x}" for x in range(1, 5)]
    # leaf to spine fabric
    for leaf in leaves:
        for spine in spines:
            g.add_edge(leaf, spine)
    # "border" leaf
    for leaf in leaves[:2]:
        for core in cores:
            g.add_edge(leaf, core)
    # core to sum
    for core in cores:
        for summ in sums:
            g.add_edge(core, summ)
    # dist to summ
    for summ in sums:
        for dist in dists:
            g.add_edge(dist, summ)
    # dist to edge
    for dist in dists[-2:]:
        for edge in edges:
            g.add_edge(dist, edge)
    # inter-dist links
    for idx in range(0, len(dists), 2):
        g.add_edge(dists[idx], dists[idx + 1])
    g.add_edge("sum1", "sum2")
    g.add_edge("edge1", "edge2")
    g.add_edge("edge3", "edge4")
    return g

def draw_small():
    """Draw my pet graph."""
    g = nx.Graph()
    g.add_edges_from([("A", "B"), ("A", "D"), ("B", "C"), ("D", "C"), ("D", "E"), ("D", "F")])
    return g

def draw_wiki():
    """Draw the graph from https://en.wikipedia.org/wiki/Biconnected_component"""
    g = nx.Graph()
    g.add_edges_from(
        [
            ("A", "B"),
            ("A", "J"),
            ("B", "C"),
            ("B", "I"),
            ("B", "H"),
            ("H", "G"),
            ("H", "F"),
            ("E", "F"),
            ("E", "D"),
            ("E", "C"),
            ("D", "C"),
            ("J", "K"),
            ("K", "N"),
            ("K", "L"),
            ("M", "N"),
            ("L", "M"),
        ]
    )
    return g

@pytest.fixture
def gen_nodes():
    """Generate nodes from graph class for individual tests."""
    params = [
        (draw_wiki(), {"A", "B", "H", "J", "K"}),
        (draw_small(), {"D"}),
        (draw_network(), set()),
    ]
    for tup in params:
        for node in tup[0].nodes:
            yield tup[0], node, tup[1]

@pytest.mark.parametrize("graph,node,expected", gen_nodes())
def test_tarjan(graph, node, expected):
    assert tarjan(graph, node)[2] == expected


def main():
    """For testing with iPython"""
    # nx.draw_spring(g, with_labels=True)
    dfs = nx.Graph()
    # for k, v in tarjan(draw_network(), "sum1")[0].items():
    # for k, v in tarjan(draw_small(), "A")[0].items():
    for k, v in tarjan(draw_wiki(), "A")[0].items():
        dfs.add_edge(k, v)
    nx.draw_spring(dfs, with_labels=True)

if __name__ == "__main__":
    main()
