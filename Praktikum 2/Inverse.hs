inverse :: [Char] -> [Char]

inverse l = 
    if length l == 0 then
        []
    else
        inverse (tail l) ++ [head l]