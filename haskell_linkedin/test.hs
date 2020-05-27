-- main :: IO()
-- main = putStrLn "Hello world"
-- 
-- data Compass = North | East | South | West
-- 
-- instance Show Compass where
--   show North = "North"
--   show East = "East"
--   show West = "West"
--   show South = "South"
-- 
-- data Expression = Number Int
--                 | Add Expression Expression
--                 | Subtract Expression Expression
--                 deriving (Eq, Ord, Show)
-- 
-- calculate :: Expression -> Int
-- calculate (Number x) = x
-- calculate (Add x y) = (calculate x) + (calculate y)
-- calculate (Subtract x y) = (calculate x) - (calculate y)
-- 
-- data F a = Leaf
--          | Node a a
--     deriving Show
-- stack script --resolver lts-12.21
import           Data.Aeson.Parser           (json)
import           Data.Conduit                (($$))
import           Data.Conduit.Attoparsec     (sinkParser)
import           Network.HTTP.Client
import           Network.HTTP.Client.Conduit (bodyReaderSource)
import           Network.HTTP.Client.TLS     (tlsManagerSettings)
import           Network.HTTP.Types.Status   (statusCode)

main :: IO ()
main = do
    manager <- newManager tlsManagerSettings

    request <- parseRequest "http://httpbin.org/get"

    withResponse request manager $ \response -> do
        putStrLn $ "The status code was: " ++
                   show (statusCode $ responseStatus response)

        value <- bodyReaderSource (responseBody response)
              $$ sinkParser json
        print value
