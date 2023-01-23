module ListOfCharacter where

{-
inverse :: [Char] -> [Char]

inverse l =
    if length l == 0 then
        []
    else
        inverse (tail l) ++ [head l]

        -}

makeUnique :: [Char] -> [Char]

ceksama :: [Char] -> Char -> Bool 

ceksama l c = 
    if length l == 0 then
        False
    else if head l == c then
        True
    else
        ceksama (tail l) c

makeUnique l =
    if length l == 0 then
        []
    else
        if ceksama (init l) (last l) == True then
            makeUnique (init l) ++ []
        else
            makeUnique (init l) ++ [last l]