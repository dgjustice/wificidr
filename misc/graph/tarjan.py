"""Tarjan algorithm"""
from collections import namedtuple, defaultdict, deque

def tarjan(graph, cur_node):
    """Create a depth-first forest given a node in a graph."""
    todo_tup = namedtuple("todo_tup", "parent, neigh")
    visited = dict()
    low = dict()
    depth = 0
    parents = dict()
    todo = []
    prev_node = None
    parent_stack = []
    successors = defaultdict(set)
    ap_nodes = set()
    while cur_node:
        neighs = set(graph.neighbors(cur_node)) - set(visited.keys())
        visited[cur_node] = depth
        low[cur_node] = depth
        if prev_node is not None:
            parents[cur_node] = prev_node
            successors[prev_node].add(cur_node)
        depth += 1
        if neighs:
            prev_node = cur_node
            cur_node = neighs.pop()
            parent_stack.append(prev_node)
            if neighs:
                todo.extend([todo_tup(prev_node, neigh) for neigh in neighs])
            continue
        process_nodes = deque([cur_node])
        cur_node = None
        while todo and not cur_node:
            node = todo.pop()
            if node.neigh in visited:
                continue
            while parent_stack[-1] != node.parent:
                process_nodes.append(parent_stack.pop())
            prev_node = node.parent
            depth = visited[prev_node] + 1
            cur_node = node.neigh
        if not cur_node:
            process_nodes.extend(reversed(parent_stack))
        while process_nodes:
            node = process_nodes.popleft()
            neighs = set(graph.neighbors(node))
            if parents.get(node):
                neighs -= {parents[node]}
            for nei in neighs:
                low[node] = min(low[node], low[nei])
                if nei in successors[node] and low[nei] >= visited[node]:
                    if parents.get(node):
                        ap_nodes.add(node)
                    elif len(successors[node]) > 1:
                        ap_nodes.add(node)
    return parents, visited, ap_nodes
