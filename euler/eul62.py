from math import log
from collections import defaultdict

def find_it():
    num = 400
    sols = defaultdict(list)
    while num < 100000:
        cube_str = "".join(sorted(str(num**3)))
        sols[cube_str].append(num)
        if len(sols[cube_str]) == 5:
            print(sols[cube_str])
            print(min(sols[cube_str])**3)
            return
        num += 1

if __name__ == '__main__':
    find_it()
