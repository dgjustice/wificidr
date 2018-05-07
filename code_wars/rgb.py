def rgb(r, g, b):
  r, g, b = [i if i >= 0 else 0 for i in [r,g,b]]
  r, g, b = [i if i <= 255 else 255 for i in [r,g,b]]
  return reduce(lambda x, y: x + y, map(lambda x: hex(x).lstrip('0x').upper().zfill(2), [r,g,b]))

print rgb(-10,258,8)
