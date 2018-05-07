from sort import Sort, Selection, Insertion, Shell, Merge
import random
import pytest
import time

def timeit(method):
    """'Borrowed' from https://medium.com/pythonhive/python-decorator-to-
    measure-the-execution-time-of-methods-fa04cb6bb36d"""
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print('%r  %2.2f ms' % \
                  (method.__name__, (te - ts) * 1000))
        return result

    return timed

@timeit
def do_sort(some_list):
    some_list.sort()

@pytest.fixture
def unsorted():
    return [random.randint(0, 100) for i in range(1000)]

def test_sort_is_sorted(unsorted):
    assert Sort(unsorted).is_sorted() is False
    assert Sort(list(range(100))).is_sorted()

def test_sort_selection(unsorted):
    dummy_class = Selection(unsorted)
    print("\nSelection: ")
    do_sort(dummy_class)
    assert dummy_class.is_sorted()

def test_sort_insertion(unsorted):
    dummy_class = Insertion(unsorted)
    print("\nInsertion: ")
    do_sort(dummy_class)
    assert dummy_class.is_sorted()

def test_sort_insertion2():
    t_len = 1000
    test_list = list(range(0, t_len))
    dummy_class = Insertion(test_list)
    # Screw up 10% of the values
    for i in range(t_len // 10):
        v1 = random.randint(0, t_len - 1)
        v2 = random.randint(0, t_len - 1)
        dummy_class.exch(v1, v2)
    dummy_class = Insertion(test_list)
    print("\nInsertion2: ")
    do_sort(dummy_class)
    assert dummy_class.is_sorted()

def test_sort_shell(unsorted):
    dummy_class = Shell(unsorted)
    print("\nShell: ")
    do_sort(dummy_class)
    assert dummy_class.is_sorted()

def test_sort_merge_topdown(unsorted):
    dummy_class = Merge(unsorted)
    print("\nMerge top down: ")
    do_sort(dummy_class)
    assert dummy_class.is_sorted()

def test_sort_merge_bottomup(unsorted):
    dummy_class = Merge(unsorted)
    print("\nMerge bottom up: ")
    dummy_class.sort(method="bu")
    assert dummy_class.is_sorted()
