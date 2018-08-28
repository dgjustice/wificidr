"""Euler 22"""

with open("names.txt", "r") as fp:
    # Read, strip quotes, lowerize, make a list, sort
    data = fp.read().replace('"', "").lower().split(",")
    data.sort()

name_score = lambda s: sum([ord(c) - 96 for c in s])

sum_scores = 0
for idx, name in enumerate(data):
    sum_scores += name_score(name) * (idx + 1)

print(sum_scores)
