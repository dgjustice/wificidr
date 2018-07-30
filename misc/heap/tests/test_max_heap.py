"""Heap test."""
from random import randint
import pytest
from heap import MaxHeap

MAX_ITER = 100

@pytest.fixture
def test_heap():
    """Pytest fixture."""
    heap = MaxHeap()
    for _ in range(MAX_ITER):
        heap.insert(randint(0, 100))
    return heap

@pytest.mark.parametrize("count", range(MAX_ITER // 2))
def test_pos(count, test_heap):
    """Test exchange method."""
    pos = randint(0, len(test_heap.heap) - 1)
    val = test_heap.heap[pos]
    assert pos == test_heap.pos(val)

@pytest.mark.parametrize("count", range(MAX_ITER // 2))
def test_exch(count):
    """Test exchange method."""
    heap = MaxHeap()
    _ = [heap.insert(randint(0, 100)) for i in range(MAX_ITER)]
    pos_a = randint(0, len(heap.heap) - 1)
    val_a = heap.heap[pos_a]
    pos_b = randint(0, len(heap.heap) - 1)
    val_b = heap.heap[pos_b]
    heap.exch(val_a, val_b)
    assert heap.heap[pos_a] == val_b and heap.heap[pos_b] == val_a

def test_insert(test_heap):
    """Test heap insert and max."""
    assert test_heap.heap[0] == max(test_heap.heap)

@pytest.mark.parametrize("count", range(MAX_ITER // 2))
def test_pop_is_max(count, test_heap):
    """Test pop is maximum value."""
    for _ in range(len(test_heap.heap)):
        max_val = max(test_heap.heap)
        popped_val = test_heap.pop()
        assert max_val == popped_val

def test_pop_all_sorted(test_heap):
    """Pop all should return reverse ordered set."""
    heap_len = len(test_heap.heap)
    test_list = [test_heap.pop() for i in range(heap_len)]
    assert test_list == sorted(set(test_list), reverse=True)
