module ListOfInteger where

listPlus :: [Int] -> [Int] -> [Int]

listPlus k l =
    if (length k == 0) && (length l == 0) then
        []
    else
        [(head l) + (head k)] ++ listPlus (tail k) (tail l)