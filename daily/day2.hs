myList = [3, 2, 1]

partSplit = (\n -> splitAt n)
prodParts = (\x -> product (init (fst x) ++ snd x))

outList = [prodParts (partSplit n myList) | n <- [1..length(myList)]]
