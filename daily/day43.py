"""
Implement a stack that has the following methods:

push(val), which pushes an element onto the stack
pop(), which pops off and returns the topmost element of the stack. If there are 
no elements in the stack, then it should throw an error or return null.
max(), which returns the maximum value in the stack currently. If there are no 
elements in the stack, then it should throw an error or return null.
Each method should run in constant time.
"""

class Stack:
    def __init__(self, val=[]):
        self.arr = val

    def push(self, val):
        self.arr.append(val)
        return None

    def pop(self):
        if self.arr:
            ret_val = self.arr[-1]
        else:
            ret_val = None
        self.arr = self.arr[:-1]

    def max(self):
        # Assumex homogeneous data types
        if not self.arr:
            return None
        max_val = self.arr[0]
        for i in self.arr:
            if i > max_val:
                max_val = i
        return max_val

def test_stack():
    s = Stack()
    s = Stack([1, 3, 9])

def test_stack_push():
    s = Stack()
    s.push(3)
    s.push(99)
    s.push("foo")
    assert s.arr == [3, 99, "foo"]

def test_stack_pop():
    s = Stack(["hello", 3, 42, "Bob"])
    while s.arr:
        s.pop()
    assert not s.arr

def test_stack_max():
    s = Stack(list(range(100)))
    assert s.max() == 99
