DIRECTIONS = {
    "left": (0, -1),
    "right": (0, 1),
    "down": (1, 0),
    "up": (-1, 0),
}
MOVES = ["right", "down", "left", "up"]

def turner():
    """Clock number generator"""
    counter = 0
    while True:
        yield counter % 4
        counter += 1

def spiral_print(matrix):
    """Print a 2x matrix in a spiral"""
    rows = len(matrix)
    cols = len(matrix[0])
    max_steps = rows * cols
    row = 0
    col = -1
    turn_it = turner()
    cur_dir = MOVES[next(turn_it)]
    while max_steps:
        if cur_dir in ["left", "right"]:
            steps = cols
            rows -= 1
        else:
            steps = rows
            cols -= 1
        for _ in range(steps):
            col += DIRECTIONS[cur_dir][1]
            row += DIRECTIONS[cur_dir][0]
            # print("r", row, "c", col, "step", steps)
            print(matrix[row][col])
            max_steps -= 1
        cur_dir = MOVES[next(turn_it)]

def test_spiral_print(capsys):
    """Test given case"""
    m = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]
    ]
    spiral_print(m)
    captured = capsys.readouterr()
    assert captured.out == """1
2
3
4
5
10
15
20
19
18
17
16
11
6
7
8
9
14
13
12
"""

def test_spiral_print2(capsys):
    """Corner case"""
    m = [[1]]
    spiral_print(m)
    captured = capsys.readouterr()
    assert captured.out == """1\n"""

m = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
]
spiral_print(m)
