"""
Suppose an arithmetic expression is given as a binary tree. Each leaf is an
integer and each internal node is one of '+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

    *
   / \
  +    +
 / \  / \
3  2  4  5
You should return 45, as it is (3 + 2) * (4 + 5).
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

TREE = Node(
    "*",
    Node(
        "+",
        Node(3),
        Node(
            2,
            # Node(8),
            # Node(9)
        )
    ),
    Node(
        "+",
        Node(4),
        Node(5)
    )
)

def calculate(root):
    queue = []
    to_do = []
    cur_node = root
    while cur_node:
        queue.append(cur_node.val)
        if cur_node.right:
            to_do.append(cur_node.right)
        if cur_node.left:
            cur_node = cur_node.left
            continue
        if not cur_node.left:
            if to_do:
                cur_node = to_do.pop()
            else:
                cur_node = None

    ops = []
    args = []
    for idx, item in enumerate(queue):
        if item in {"*", "/", "+", "-"}:
            ops.append(item)
        else:
            if queue[idx - 1] not in {"*", "/", "+", "-"}:
                args.append(item)
                while len(args) > 1:
                    op = ops.pop()
                    arg1 = args.pop()
                    arg2 = args.pop()
                    args.append(eval(f"{arg1} {op} {arg2}"))
            else:
                args.append(item)
    return args[0]


def test_tree():
    assert calculate(TREE) == 45

print(calculate(TREE))
