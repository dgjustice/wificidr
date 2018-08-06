"""Playing with heaps."""


class Heap:
    """A heap class."""

    def __init__(self):
        """Initialize the heap."""
        self.heap = []
        self.items = set()

    def exch(self, val, other):
        """Exchange two elements."""
        val_pos = self.pos(val)
        other_pos = self.pos(other)
        tmp = self.heap[val_pos]
        self.heap[val_pos] = self.heap[other_pos]
        self.heap[other_pos] = tmp

    def pos(self, val) -> int:
        """Return position."""
        return self.heap.index(val)

    @staticmethod
    def less(val, other):
        """Return is val < other."""
        if val is None or other is None:
            return True
        return val < other

    @staticmethod
    def largest(item_list):
        """Return the maximum item."""
        return max(item_list)

    def parent(self, val):
        """Return the position of the parent in the heap."""
        pos = self.pos(val)
        # Head of list has no parent
        if not pos:
            return val
        if not pos % 2:
            return self.heap[((pos - 1) >> 1)]
        return self.heap[(pos >> 1)]

    def children(self, val):
        """Return the children of a node."""
        pos = self.pos(val)
        ldx = pos * 2 + 1
        rdx = (pos * 2) + 2
        heap_len = len(self.heap)
        lchild = self.heap[ldx] if heap_len > ldx else None
        rchild = self.heap[rdx] if heap_len > rdx else None
        return lchild, rchild


class MaxHeap(Heap):
    """Maximum ordered heap."""

    def insert(self, val):
        """Insert a value into the heap."""
        if val not in self.items:
            self.items.add(val)
            self.heap.append(val)
            self.swim(val)

    def swim(self, val):
        """Float a key up."""
        if len(self.heap) <= 1:
            return
        parent = self.parent(val)
        while not self.less(val, parent) and parent != val:
            self.exch(val, parent)
            parent = self.parent(val)

    def sink(self, parent):
        """Sink a key down."""
        if len(self.heap) <= 1:
            return
        children = [child for child in self.children(parent) if child]
        while children:
            max_child = self.largest(children)
            if self.less(parent, max_child):
                self.exch(max_child, parent)
            else:
                return
            children = [child for child in self.children(parent) if child]

    def pop(self, val=None):
        """Remove the a value (default = max) and rebalance."""
        rv = self.heap[0] if val is None else val
        last = self.heap.pop()
        if self.heap:
            self.heap[self.pos(rv)] = last
            self.sink(last)
        self.items.remove(rv)
        return rv


class MinHeap(MaxHeap):
    """
    Minimum ordered heap.

    Note that we have to swap the logic of a couple methods to change order.
    """

    @staticmethod
    def less(val, other):
        """Return is val < other."""
        if val is None or other is None:
            return True
        return val > other

    @staticmethod
    def largest(item_list):
        """Return the minimum item."""
        return min(item_list)
