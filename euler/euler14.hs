-- n → n/2 (n is even)
-- n → 3n + 1 (n is odd)

collatz :: (Integral n, Ord n) => n -> [n]
collatz n
  | n /= 1 && mod n 2 == 0 = n:collatz (quot n 2)
  | n /=1 = n:collatz (3 * n + 1)
  | otherwise = [n]

collatzMax :: (Ord n) => [(n, n)] -> (n, n)
collatzMax [x] = x
collatzMax (x:xs)
    | snd x > snd maxTail = x 
    | otherwise = maxTail
    where maxTail = collatzMax xs

-- naive implementation, takes forever.  Will rewrite with lookup table
foo = collatzMax ([(n, length(collatz n)) | n <- [1..999999]])
