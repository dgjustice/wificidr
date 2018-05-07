def to_camel_case(text):
  l = list(text)
  i = 0
  while i < len(l):
    if l[i] == '-' or l[i] == '_':
      l.pop(i)
      if i < len(l):
        l[i] = l[i].upper() if i != 0 else l[i]
    i += 1
  return reduce(lambda x, y: x + y, l)

print to_camel_case("_this-isnt_cool-")
