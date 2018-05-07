import fractions

def lcm(*args): 
  if len(args) == 1:
    return args[0]
  i = 0
  b = args[i + 1]
  while i + 1 <= len(args):
    a = args[i]
    r = abs(a * b) / fractions.gcd(a,b) if a and b else 0
    b = r
    i += 1
  return r

print lcm(2,3,4, 5)
