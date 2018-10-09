"""
An XOR linked list is a more memory efficient doubly linked list. Instead of each node 
holding next and prev fields, it holds a field named both, which is an XOR of the next 
node and the previous node. Implement an XOR linked list; it has an add(element) which 
adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access 
to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.
"""

import weakref
from pdb import set_trace

_id2obj_dict = weakref.WeakValueDictionary()

def remember(obj):
    oid = id(obj)
    _id2obj_dict[oid] = obj
    return oid

def id2obj(oid):
    return _id2obj_dict[oid]

class Node:
    def __init__(self, val):
        remember(self)
        self.val = val
        self.both = 0

    def get_next(self, prev):
        """Return the next object."""
        print("??", prev, self.both)
        next_id = self.both ^ prev
        if not next_id or next_id == prev:
            return None
        return next_id

class DoubleList:
    def __init__(self):
        root = Node("root")
        self.root = root

    def __getitem__(self, index):
        for idx, val in enumerate(self):
            if idx == index:
                return id2obj(val)
        raise IndexError

    def add(self, other):
        """Add an element to the end of the list."""
        for obj in self:
            pass
        print("val", obj.val)
        print("before", obj.both, other.both)
        obj.both = obj.both ^ id(other)
        other.both = id(obj)
        print("after", obj.both, other.both)

    def __iter__(self):
        cur_id = id(self.root)
        yield _id2obj_dict[cur_id]
        prev = 0
        while cur_id is not None:
            next_id = id2obj(cur_id).get_next(prev)
            if next_id:
                yield id2obj(next_id)
            prev = cur_id
            cur_id = next_id

if __name__ == "__main__":
    xll = DoubleList()
    other = Node("two")
    xll.add(other)
    nother = Node("three")
    xll.add(nother)
    print([i.val for i in xll])
