module LamaTidur where

-- Juan Christopher Santoso
-- 16521098
-- menghitung waktu lama tidur              lamaTidur(a,b,c)

-- Definisi dan Spesifikasi
lamaTidur :: Int -> Int -> Int -> (Bool, Int, Int, Int)

{- fungsi lamaTidur memiliki 3 input yang bertipe integer. Input mengeluarkan output sebuah tuple
yang berisi 1 data bool dan 3 data integer. 4 data ini berisikan informasi apakah orang tersebut mampu
tidur cukup lebih dari 6 jam dan lama tidurnya. -}

-- Realisasi
lamaTidur a b c =
    if a < 5 then -- rentang waktu tidur start tidur antara jam 12 malam hingga jam 5
        let lamaDetik = a*3600 + b*60 + c
            durasi = 5*3600 - lamaDetik
            x = durasi `div` 3600
            y = (durasi - x*3600) `div` 60
            z = durasi - x*3600 - y*60
        in
            if durasi >= 6*3600 then
                (True, x, y, z)
            else
                (False, x, y, z)
    else
        let lamaDetik = a*3600 + b*60 + c
            durasi = 5*3600 + (24*3600 - lamaDetik)
            x = durasi `div` 3600
            y = (durasi - x*3600) `div` 60
            z = durasi - x*3600 - y*60
        in
            if durasi >= 6*3600 then
                (True, x, y, z)
            else
                (False, x, y, z)
                
