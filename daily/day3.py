"""
Given the root to a binary tree, implement serialize(root), which serializes the 
tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
   def __init__(self, val, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""
import json

class Node:
   def __init__(self, val, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right

def serialize(node):
    out = dict(val=node.val)
    if node.right: out["right"] = serialize(node.right)
    if node.left: out["left"] = serialize(node.left)
    return out

def deserialize(node_dict):
    left = None
    right = None
    if node_dict.get("left"):
        left = deserialize(node_dict["left"])
    if node_dict.get("right"):
        right = deserialize(node_dict["right"])
    return Node(node_dict["val"], left, right)

def test_serialize():
    node_dict = {
        "val": "root",
        "left": {
            "val": "left",
            "left": {
                "val": "left.left"
            }
        },
        "right": {
            "val": "right"
        }
    }
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert serialize(node) == node_dict

def test_deserialize():
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
