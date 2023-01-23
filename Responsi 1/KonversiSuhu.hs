module KonversiSuhu where

konversiSuhu :: Float -> Char -> Float

konversiSuhu a b = 
    if b == 'R' || b == 'r' then
        a * 4/5
    else if b == 'F' || b == 'f' then
        (a * 9/5) + 32
    else if b == 'K' || b == 'k' then
        (a + 273.15)
    else 
        a 