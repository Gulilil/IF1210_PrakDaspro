module ListOfInteger where

setDiff :: [Int] -> [Int] -> [Int]

ceksama :: [Int] -> Int -> Bool 

ceksama l n =
    if length l == 0 then
        False 
    else if head l == n then
        True 
    else
        ceksama (tail l) n

setDiff k l =
    if length k == 0 then
        []
    else
        if ceksama l (head k) == True then
            [] ++ setDiff (tail k) l
        else
            [head k] ++ setDiff (tail k) l 
