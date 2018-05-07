from __future__ import print_function
import json


class Node(object):
    '''
        Linked-list class for GCD extended method
    '''
    def __init__(self, key, factor, num):
        self._key = key
        self._factor = factor
        self._pos = None
        self._neg = None
        self._num = num
    def add_pos(self, node):
        self._pos = node
    def add_neg(self, node):
        self._neg = node
    @property
    def key(self):
        return self._key
    @property
    def factor(self):
        return self._factor
    @property
    def num(self):
        return self._num

def gcd(a, b):
    '''
        Finds the GCD between two numbers using Euclid's method
    '''
    big_num = a if a > b else b
    small_num = b if b < a else a
    remainder = 1
    while remainder != 0:
        remainder = big_num % small_num
        big_num = small_num
        small_num = remainder
    return big_num

def gcd_extended(a, b):
    '''
        Finds linear combination and GCD using Euclid's method
        gcd = sa + tb
        returns tuple of (gcd, (a, s), (b, t))
    '''
    big_num = a if a > b else b
    small_num = b if b < a else a
    remainder = 1
    factors = dict()
    while remainder != 0:
        remainder = big_num % small_num
        factors[remainder] = dict(pos=dict(val=big_num, fac=1), neg=dict(val=-1*small_num, fac=big_num//small_num))
        big_num = small_num
        small_num = remainder
    gcd = big_num
    root = Node(gcd, 1, 1)
    n = root
    nodes = []
    # Expand the tree
    results = {a: {'fac': 0}, b: {'fac': 0}}
    multipliers = []
    num = 1
    while n:
        try:
            num = n.num
            if n.key >= 0:
                pos = Node(factors[abs(n.key)]['pos']['val'], factors[abs(n.key)]['pos']['fac'], num * 2)
                neg = Node(factors[abs(n.key)]['neg']['val'], factors[abs(n.key)]['neg']['fac'], (num * 2) + 1)
            else:
                neg = Node(factors[abs(n.key)]['pos']['val']*(-1), factors[abs(n.key)]['pos']['fac'], (num * 2) + 1)
                pos = Node(factors[abs(n.key)]['neg']['val']*(-1), factors[abs(n.key)]['neg']['fac'], num * 2)
            f = n.factor
            n = neg
            if n.num % num == 1:
                multipliers.append(f)
            nodes.append(pos)
            oldnum = num
        except KeyError:
            z = 1
            for q in multipliers:
                z *= q
            results[abs(n.key)]['fac'] += z * n.key / (abs(n.key)) * n.factor
            try:
                n = nodes.pop()
                if num // n.num != 1:
                    multipliers.pop()
            except IndexError:
                n = False
    return (gcd, (a, results[a]['fac']), (b, results[b]['fac']))

if __name__ == "__main__":
    # Some test cases in lieu of a proper test
    # print(gcd(12, 30))
    # print(gcd(30, 12))
    # print(gcd(216, 594))
    # print(gcd(594, 216))
    # print(gcd(31, 216))
    print(gcd_extended(1350, 297))
    print(gcd_extended(98, 273))
    print(gcd_extended(108, 60))
