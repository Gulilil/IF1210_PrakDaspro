module Max3 where

-- Mencari Nilai Maksimum               max3(a,b,c)

-- Definisi dan Spesifikasi
max3 :: Int -> Int -> Int -> Int 
{- Fungsi max3 memiliki 3 input yang bertipe Integer yang berbeda. Fungsi tersebut
akan mengeluarkan output yang bertipe Integer. Fungsi tersebut akan mengeluarkan output
nilai terbesar dari ketiga nilai yang diinputkan -}
-- Tidak boleh membuat fungsi antara

-- Realisasi
max3 a b c =
    if a >= b && a >= c then
        a
    else if b >= a && b >=c then
        b
    else
        c