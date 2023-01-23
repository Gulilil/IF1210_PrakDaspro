module OffsetList where

-- Definisi dan Spesifikasi
offsetList :: [Int] -> (Int -> Int) -> [Int]
plus2 :: Int -> Int 
minus1 :: Int -> Int 
offKond :: Int -> Int

{-
Dengan fungsi offset plus2, akan menghasilkan list baru dengan nilai setiap elemen yang sudah bertambah 2
Dengan fungsi offset minus1, akan menghasilkan list baru dengan nilai setiap elemen yang sudah berkurang 1
Dengan fungsi offset offKond, akan menghasilkan list baru dengan nilai setiap elemen yang diubah sesuai ketentuan range tertentu -}

plus2 x = x + 2
minus1 x = x - 1
offKond x = 
    if x >= 0 && x <= 40 then
        10
    else if x < 0 then
        0
    else -- x>40
        20

offsetList l f =
    if length l == 0 then -- Basis
        []
    else -- Rekurens
        [f (head l)] ++ offsetList (tail l) f
