import Control.Applicative
import Control.Monad
import System.IO


main :: IO ()
main = do
    base_temp <- getLine
    let base_t = words base_temp
    let base = read $ base_t!!0 :: Int
    let area = read $ base_t!!1 :: Int
    let tri = \a b -> ceiling (fromIntegral(2 * a) / fromIntegral(b))
    print (tri area base)

getMultipleLines :: Int -> IO [String]

getMultipleLines n
    | n <= 0 = return []
    | otherwise = do          
        x <- getLine         
        xs <- getMultipleLines (n-1)    
        let ret = (x:xs)    
        return ret
