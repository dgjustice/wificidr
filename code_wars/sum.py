#Sum of Pairs

def sum_pairs(ints, s):
  c = 0
  sol = [None, None]
  for i in range(0, len(ints)):
    for q in range(i, len(ints)):
      if ints[i] + ints[q] == s and i != q and i < q:
        if None in sol or q < sol[1]:
          sol = [i, q]
  if None in sol:
    return None
  else:
    return [ints[sol[0]], ints[sol[1]]]

if __name__ == "__main__":
  l1= [1, 4, 8, 7, 3, 15]
  #print(sum_pairs(l1, 8))
  print(sum_pairs([10, 5, 2, 3, 7, 5], 10))
