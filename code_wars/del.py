# Code Wars Delete Nth occurrence of element
def delete_nth(order,max_e):
  # code here
  output = []
  t = {}
  for i in range(0, len(order)):
    try:
      t[order[i]] += 1
    except:
      t[order[i]] = 1
    if t[order[i]] <= max_e:
      output.append(order[i])
  return output
  
if __name__ == "__main__":
  print(delete_nth([20,37,20,21], 1))
  print(delete_nth([1,1,3,3,7,2,2,2,2], 3))
