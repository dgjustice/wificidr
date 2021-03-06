from ipaddress import ip_network
from typing import Optional, Any
root_block = ip_network("147.75.38.0/23")
# data = []


# def load_data():
#     for row in text.split("\n"):
#          data.append(ip_network(row.split("\t")[0].strip()))


class CIDRnode:
    def __init__(self, subnet: Any, attr: Optional[str] = None) -> None:
        self.subnet = subnet
        self.attr = attr
        self.left: Optional[CIDRnode] = None
        self.right: Optional[CIDRnode] = None


def split_node(node: CIDRnode) -> None:
    subs = node.subnet.subnets(prefixlen_diff=1)
    node.left = CIDRnode(next(subs), "free")
    node.right = CIDRnode(next(subs), "free")
    if node.attr == "free":
        node.attr = ""


def allocate_node(root: CIDRnode, prefixlen: int) -> Any:
    if root.subnet.prefixlen == prefixlen:
        if root.attr == "allocated":
            return None
        elif root.attr == "free":
            root.attr = "allocated"
            return root
    if root.subnet.prefixlen >= prefixlen:
        return None
    if root.attr == "free":
        split_node(root)
    if root.left and root.right:
        return allocate_node(root.left, prefixlen) or allocate_node(root.right, prefixlen)


def xor_nets(parent: Any, child: Any) -> int:
    return (int(parent.network_address) >> (32 - parent.prefixlen)) ^ \
           (int(child.network_address) >> (32 - parent.prefixlen))


def add_node(root: CIDRnode, child: Any) -> Any:
    if root.subnet >= child:
        if root.attr == "allocated":
            return None
        else:
            root.attr = "allocated"
            return root
    if not root.left and not root.right:
        split_node(root)
    # mypy happiness
    assert root.left is not None and root.right is not None
    if xor_nets(root.left.subnet, child) == 0:
        return add_node(root.left, child)
    return add_node(root.right, child)


# root = CIDRnode(root_block)
# load_data()
# # print(f"allocated: {allocate_node(root, 32).subnet}")
# for row in data:
#     add_node(root, row)
# # print(add_node(root, ip_network("147.75.38.128/31")).subnet)<Paste>
#
#
# # Build pretty pictures and export to cytoscape
# import networkx as nx
#
# g = nx.Graph()
#
#
# def add_edge(node):
#     if node.left and node.right:
#         g.add_edge(str(node.subnet), str(node.left.subnet))
#         g.add_edge(str(node.subnet), str(node.right.subnet))
#         g.nodes[str(node.subnet)]["status"] = node.attr or ""
#         g.nodes[str(node.left.subnet)]["status"] = node.left.attr or ""
#         g.nodes[str(node.right.subnet)]["status"] = node.right.attr or ""
#         add_edge(node.left)
#         add_edge(node.right)
#     return
#
#
# add_edge(root)
# nx.write_gml(g, "graph.gml")
#
#
# free = []
# allocated = []
# for node in g.nodes:
#     if g.nodes[node]["status"] == "allocated":
#         allocated.append(node)
#     if g.nodes[node]["status"] == "free":
#         free.append(node)
#
# # Sanity check
# assert len(allocated) == len(data)
# for net in free:
#     print(net)
#
# print(f"There are {len(g.nodes)} nodes in the tree.")
