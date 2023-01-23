module OffsetList where

plus2 :: Int -> Int 
minus1 :: Int -> Int 
offKond :: Int -> Int 
offsetList :: [Int] -> (Int -> Int) -> [Int]

plus2 x = x+2
minus1 x = x-1
offKond x =
    if x >= 0 && x <= 40 then 10
    else if x < 0 then 0
    else 20

offsetList l f =
    if length l == 0 then
        []
    else
        [f (head l)] ++ offsetList (tail l) f