module SumOfDigits where

-- Menghitung akumulasi nilai integer           sumOfDigits(x)

-- Definisi dan Spesifikasi
sumOfDigits :: Int -> Int 
{- fungsi sumOfDigits menghitung akumulasi nilai setiap integer tunggal yang diinputkan
pada fungsi tersebut. Fungsi memiliki input dan output yang bertipe sama yaitu Integer -}
-- Prekondisi n>=0

-- Realisasi
sumOfDigits x = 
    if x < 10 then -- Basis
        x
    else -- Rekurens (x >= 10)
        sumOfDigits(x `div` 10) + x `mod` 10