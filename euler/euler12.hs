triangle n = quot (n*(n + 1)) 2
foo = [x | x <- [500..1000], length [m | m <- [1..(quot (triangle x) 2)], mod (triangle x) m == 0] > 200]
