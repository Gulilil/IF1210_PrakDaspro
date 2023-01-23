module HitungIndeks where

-- Juan Christopher Santoso 
-- 16521098 

-- Menghitung Indeks Nilai          hitungIndeks(a,b,c)

-- Definisi dan Spesifikasi
hitungIndeks :: Float -> Float -> Float -> Int
{- Fungsi hitungIndeks memiliki 3 input yang berupa Float yang merupakan representasi 
nilai siswa. (Nilai UTS, UAS, dan Tubes berturut-turut). Fungsi mengeluarkan output yang bertipe Integer 
yang merupakan representasi dari indeks siswa. -}
    -- A = 4, B = 3, C = 2, D = 1, E = 0
    -- Jika ketiga 3 >= 75, maka A 
    -- Jika hanya 1 atau 2 yang >= 75, maka B
    -- Jika nilai tubes < 40 and UTS UAS > 40, maka C
    -- Jika semua nilai >= 40 dan < 75, maka C
    -- Jika UTS atau UAS <40, maka D (tidak peduli Tubes)
    -- Jika satu nilai 0, maka auto E

-- Realisasi
hitungIndeks a b c =
    -- Urutan skala prioritas
    if a >= 75 && b >= 75 && c >= 75 then -- Kondisi 1
        4
    -- Kondisi 1 tidak mgkin sama dengan kondisi 6
    else if a == 0 || b == 0 || c== 0 then -- Kondisi 6
        0
    -- Ada 1 nilai 0, maka auto E
    else if a < 40 || b < 40 then -- Kondisi 5
        1
    else if a >= 40 && b >= 40 && c < 40 then --Kondisi 3
            2
    else if (a > 40 && a < 75) && (b > 40 && b < 75) && (c > 40 && c < 75) then
        2
    else -- a > 75 || b > 75 || c> 75
        3
        
