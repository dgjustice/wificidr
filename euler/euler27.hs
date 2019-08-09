-- Stolen from the Haskell wiki
isPrime n = n > 1 &&
              foldr (\p r -> p*p > n || ((n `rem` p) /= 0 && r))
                True primes

primes = 2 : filter isPrime [3,5..]

-- Considering quadratics of the form:
-- 
--     n^2+an+b
-- 
-- , where |a|<1000 and |b|≤1000
-- 
-- where |n|
-- is the modulus/absolute value of n
-- e.g. |11|=11 and |−4|=4
-- 
-- Find the product of the coefficients, a
-- and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.

-- The equation
quad:: (Int, Int) -> Int -> Int
quad (a, b) n = n^2 + (a * n) + b

-- All combinations of (a, b)
abcomb = [(a, b) | a <- [-999..999], b <- [-1000..1000]]

-- Find max consecutive n primes (from 0)
findPrimes :: Int -> (Int, Int) -> Int
findPrimes n (_, _)
  | n > 1000 = -1
findPrimes n (a, b)
  | prime == True = findPrimes (n + 1) (a, b)
  | prime == False = n - 1
  where prime = isPrime (quad (a, b) n)

maxInts = map (findPrimes 0) abcomb
maxInt = maximum maxInts
items = zip maxInts abcomb
maxItem = [x | x <- zip (map (findPrimes 0) abcomb) abcomb, fst x == maxInt]
