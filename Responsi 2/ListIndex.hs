module ListIndex where

listIndex :: [Int] -> (Int -> Char) -> [Char]
nilai :: Int -> Char 

nilai n =
    if n >= 80 then 'A'
    else if n >= 70 then 'B'
    else if n >= 65 then 'C'
    else if n >= 55 then 'D'
    else 'E'

listIndex l f =
    if length l == 0 then
        []
    else
        [f (head l)] ++ listIndex (tail l) f