module HappyFive where

happyFive :: [Int] -> [Int]

-- Definisi
{- Tuan Vin menyukai angka 5. Hanya angka-angka yang berhubungan dengan 5 yang dapat membuat Tuan Vin senang.

Bantulah Tuan Vin untuk membuang setiap angka yang tidak berhubungan dengan 5 atau kelipatan dari 5 dari sebuah list agar Tuan Vin
 senang dengan nama fungsi happyFive. Angka didalam list hanya bernilai satuan atau puluhan. -}

happyFive l =
    if length l == 0 then -- Basis
        []
    else -- Rekurens
        if mod (head l) 5 == 0 || div (head l) 10 == 5 then
            [head l] ++ happyFive (tail l)
        else
            [] ++ happyFive (tail l)