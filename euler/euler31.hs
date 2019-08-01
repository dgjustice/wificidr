coins = [200, 100, 50, 20, 10, 5, 2, 1]
-- coins = [5, 2, 1]

-- sublist takes [3, 2, 1] and returns [[3, 2, 1], [2, 1], [1]]
sublist :: (Num a) => [a] -> [[a]]
sublist [a] = [[a]]
sublist (x:xs) = [x:xs] ++ sublist xs

countWithCoins :: (Num a, Ord a) => a -> [a] -> a
countWithCoins _ [1] = 1
countWithCoins target (x:xs)
  | diff > 0 = sum (countWithCoins' (diff, x:xs))
  | diff == 0 = 1
  | diff < 0 = 0
  where diff = target - x

countWithCoins' :: (Num a, Ord a) => (a, [a]) -> [a]
countWithCoins' (target, xx) = map (countWithCoins target) (sublist xx)

project31 = sum (countWithCoins' (200, coins))
