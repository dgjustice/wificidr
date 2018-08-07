-- Haskell version of Euler # 16
spliDigit :: (Integral n) => n -> (n, n)
-- Split an integer 12345 into (1234, 5)
spliDigit n
  | n > 0 = ((div (n - (mod n 10)) 10), (mod n 10))

digitizer :: (Integral n) => n -> [n]
digitizer n
  | fst t > 0 = (snd t):(digitizer (fst t))
  | otherwise = [(snd t)]
  where t = spliDigit n

foo = sum (digitizer (2^1000))
