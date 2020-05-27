module Test
    ( coord
    ) where

coord :: [String] -> [[(Int, Int)]]
coord s = [[(i, j) | j <- [0..(length (s !!0))]] | i <- [0..(length s)]]
