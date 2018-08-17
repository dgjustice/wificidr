-- Project euler 25, fibonacci with 1k digits

fibonacci :: (Num a, Ord a) => a -> a
fibonacci n
  | n == 1 = 1
  | n == 2 = 1
  | otherwise = fibonacci (n - 1) + fibonacci (n - 2)

-- https://wiki.haskell.org/Memoization
memoized_fib :: Int -> Integer
memoized_fib = (map fib [0 ..] !!)
   where fib 0 = 0
         fib 1 = 1
         fib n = memoized_fib (n-2) + memoized_fib (n-1)

findIt :: Int -> Integer
findIt n
  | (div (memoized_fib n) (10^999)) < 1 = findIt (n + 1)
  | otherwise = fromIntegral(n)
