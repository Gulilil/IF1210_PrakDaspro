module SumKelipatanX where

--Juan Christopher Santoso
-- 16521098
-- Menghitung kelipatan suatu pola bilangan             sumKelipatan(m,n,x)

-- Definisi dan Spesifikasi
sumKelipatan :: Int -> Int -> Int -> Int 
{- fungsi tersebut memiliki fungsi untuk mengakumulasi atau melakukan penambahan  pada suatu urutan angka.
fungsi memiliki 3 input yang bertipe integer dan output yang juga bertipe integer. -}
-- Harus rekursif
-- m <=n
-- x <= n

-- Realisasi
sumKelipatan m n x =
    let batas = if (m `div` x)*x == m then -- m adalah kelipatan x
            m
        else -- m bukan kelipatan x
            (m `div` x)*x + x
    in
        if m > n then
            0
        else -- Rekurens
            batas + sumKelipatan (batas + x) n x
    
