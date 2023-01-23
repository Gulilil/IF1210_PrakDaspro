module AlternateSort where

sortlist :: [Int] -> [Int]
findmin :: [Int] -> Int 
alternateSort :: [Int] -> [Int]

findmin l =
    if length l == 1 then
        head l
    else if head l < head (tail l) then
        findmin (tail l ++ [head l]) -- tendang kebelakang
    else
        findmin (tail l)

sortlist l =
    if length l == 0 then
        []
    else
        if head l == findmin l then
            [head l] ++ sortlist (tail l)
        else
            sortlist (tail l ++ [head l])

alternateSort l =
    let list = sortlist l
    in
        if length list == 0 then
            []
        else if length list == 1 then
            [head list]
        else
            [head list] ++ [last list] ++ alternateSort (init (tail list)) 
