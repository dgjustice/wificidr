import sys
import pdb
'''Playing with sorting algorithms.  I'm reading the Sedgwick book
that uses Java, so I'll try to make these "pythonic" as I go.'''

# TODO: docstrings, clean up layout, debug and logging

class Sort(object):
    def __init__(self, l):
        self.arr = l

    def sort(self):
        return NotImplemented
    @staticmethod
    def less(i, j):
        return i < j

    def exch(self, i, j):
        temp = self.arr[i]
        self.arr[i] = self.arr[j]
        self.arr[j] = temp

    def show(self):
        for i in range(len(self.arr)):
            print(self.arr[i])

    def is_sorted(self):
        for i, val in enumerate(self.arr[1::], 1):
            if self.arr[i - 1] > val:
                return False
        else:
            return True

class Selection(Sort):
    def sort(self):
        e = 0
        for i in range(len(self.arr)):
            low = i
            for j in range(i, len(self.arr)):
                if self.arr[j] < self.arr[low]:
                    low = j
            self.exch(i, low)
            e += 1
        print("%d exchanges" % e)

class Insertion(Sort):
    def sort(self):
        e = 0
        for i in range(1, len(self.arr)):
            for j in range(i, 0, -1):
                if self.arr[j] < self.arr[j - 1]:
                    self.exch(j, j - 1)
                    e += 1
                else:
                    break
        print("%d exchanges" % e)

class Shell(Sort):
    def sort(self):
        e = 0
        n = len(self.arr)
        h = 1
        while h < n // 3:
            h = (3 * h) + 1
        while h >= 1:
            for i in range(h, n):
                for j in range(i, h - 1, -h):
                    if self.arr[j] < self.arr[j - h]:
                        self.exch(j, j - h)
                        e += 1
                    else:
                        break
            h = h // 3
        print("%d exchanges" % e)

class Merge(Sort):
    def _merge(self, low, mid, high):
        i = low
        j = mid + 1
        for k in range(low, high + 1):
            if i > mid:
                self.arr[k] = self._aux[j]
                j += 1
            elif j > high:
                self.arr[k] = self._aux[i]
                i += 1
            elif self.less(self._aux[j], self._aux[i]):
                self.arr[k] = self._aux[j]
                j += 1
            else:
                self.arr[k] = self._aux[i]
                i += 1

    def _sort_td(self, low, high):
        if high <= low:
            return
        # pdb.set_trace()
        mid = low + ((high - low) // 2)
        self._sort_td(low, mid)
        self._sort_td(mid + 1, high)
        self._merge(low, mid, high)

    def _sort_bu(self):
        size = 1
        while size < len(self.arr):
            for low in range(0, len(self.arr) - size, size * 2):
                self._merge(
                    low, low + size - 1, min(
                        low + size * 2 - 1, len(self.arr) - 1))
            size += size
        
    def sort(self, method="td"):
        self._aux = list([0] * len(self.arr))
        if method == "td":
            self._sort_td(0, len(self.arr) - 1)
        elif method == "bu":
            self._sort_bu()
