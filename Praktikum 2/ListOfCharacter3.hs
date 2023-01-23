module ListOfCharacter3 where

-- Definisi 
{- Buatlah fungsi makeUnique yang menerima masukan sebuah list of character, misalnya lc,
 dan menghasilkan list dengan elemen-elemen unik, yaitu, kemunculan setiap elemen (jika tidak kosong), hanya 1. -}

ceksama :: Char -> [Char] -> Bool 
makeUnique :: [Char] -> [Char]

-- Realisasi
ceksama x l =
    if length l == 0 then --abis dan ga ada yg sama
        False 
    else if head l == x then -- ada yg sama
        True 
    else
        ceksama x (tail l)

makeUnique l =
    if length l == 0 then 
        []
    else
        if ceksama (last l) (init l) == True then -- yg belakang ada yg sama kek di depan
            makeUnique (init l) ++ []
        else -- kalo ga ada yg sama kek last l
            makeUnique (init l) ++ [last l]
