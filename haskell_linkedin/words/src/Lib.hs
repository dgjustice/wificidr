module Lib
    ( grid
    , languages
    , formatGrid
    , outputGrid
    , findWord
    , findWordInLine
    , findWords
    , getLines
    , diagonals
    , diagaline
    , getDiagonals
    ) where

import Data.List (isInfixOf, transpose)
import Data.Maybe (catMaybes)
import Data
type Grid = [String]

outputGrid :: Grid -> IO ()
outputGrid grid = putStrLn (formatGrid grid)

formatGrid :: Grid -> String
formatGrid = unlines

diagaline :: Grid -> Int -> Int -> String
diagaline grid x y 
  | y == 0 || x == (length(grid !!0) - 1) = [grid !!y !!x]
  | otherwise = [grid !!y !!x] ++ diagaline grid (x + 1) (y - 1)

diagonals :: Grid -> Int -> Int -> [String]
diagonals grid 0 0 = [diagaline grid 0 0]
diagonals grid x  y
  | x > 0 = [diagaline grid x y] ++ (diagonals grid (x - 1) y)
  | x == 0 = [diagaline grid x y] ++ (diagonals grid 0 (y - 1))

getDiagonals :: Grid -> [String]
getDiagonals grid =
  let x = (length(grid !!0) - 1)
      y = (length(grid) - 1)
      in diagonals grid x y ++ diagonals (map reverse grid) x y

getLines :: Grid -> [String]
getLines grid = 
  let horizontal = grid
      vertical = transpose grid
      diagonal = getDiagonals grid
      lines = horizontal ++ vertical ++ diagonal
  in lines ++ (map reverse lines)

findWord :: Grid -> String -> Maybe String
findWord grid word = 
  let lines = getLines grid
      found = or $ map (findWordInLine word) lines
      in if found then Just word else Nothing

findWordInLine :: String -> String -> Bool
findWordInLine = isInfixOf

findWords :: Grid -> [String] -> [String]
findWords grid words = catMaybes $ map (findWord grid) words
