module BuangTujuh where

buangTujuh :: [Int] -> [Int]

buangTujuh l =
    if length l == 0 then 
        []
    else
        if (mod (head l) 10 == 7) || (div (head l) 10 == 7) || (mod (head l) 7 == 0) then
            [] ++ buangTujuh (tail l)
        else
            [head l] ++ buangTujuh (tail l)