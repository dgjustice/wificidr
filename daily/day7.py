KEY = {str(i - 96): chr(i) for i in range(97, 123)}

def num_combos(string):
    str_len = len(string)
    out = 1
    for i in range(str_len - 1):
        if int(string[i:i + 2]) < 27:
            out += 2
        else:
            out += 1
    return out

def test_num_combos():
    assert num_combos('111') == 5
    assert num_combos('127') == 4
    assert num_combos('191127') == 9
