module ListOfInteger where

{-
elmtKeN :: [Int] -> Int -> Int 

elmtKeN l n =
    if n == 1 then
        head l
    else
        elmtKeN (tail l) (n-1) -}

nbOcc :: [Int] -> Int -> Int 

nbOcc l n =
    if length l == 0 then
        0
    else 
        if head l == n then
            1 + nbOcc (tail l) n
        else
            0 + nbOcc (tail l) n