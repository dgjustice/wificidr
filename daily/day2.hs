myList = [3, 2, 1]

prodErizer :: (Integral a) => [a] -> [a]
prodErizer xs = [prodParts (partSplit n xs) | n <- [2..length(xs)]]
  where partSplit = (\n -> splitAt n)
        prodParts = (\x -> product (init (fst x) ++ snd x))
