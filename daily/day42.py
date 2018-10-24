from itertools import combinations

def target_sum(input_list, target):
    for i in range(1, len(input_list) + 1):
        inner = list(combinations(input_list, i))
        for j in inner:
            if sum(j) == target:
                return inner
    return None

def test_target_sum():
    foo = [12, 1, 61, 5, 9, 2]
    assert target_sum(foo, 12)
    assert target_sum(foo, 2)
    assert target_sum(foo, sum(foo))
    assert not target_sum(foo, 999)
