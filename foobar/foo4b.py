def answer(start, length):
    out = 0
    for i in range(length, 0, -1):
        n = (length - i) * length + start
        for j in range(i):
            out ^= n
            n += 1
    return out

print(answer(1, 10000))
