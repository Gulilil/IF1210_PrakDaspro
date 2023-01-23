module HitungBensin where

hitungBensin :: Int -> Int -> Int 
hitungBiaya :: Int -> Int
-- A <= B
{- Jadi intinya disini approachnya B mendekati A. Nah, di setiap lokasi dia bakal membutuhkan sekian bensin
ngukur sekian bensinnya adalah masukin ke sebuah fungsi penghitung bensin yang berpacu pada lokasi kendaraan itu sendiri -}

hitungBensin a b =
    if a == b then --Basis 
        hitungBiaya a
    else --Rekurens
        hitungBiaya a + hitungBensin (a+1) b

hitungBiaya x =
    if x == 1 then -- Basis
        0
    else if x `mod` 2 == 0 then -- Posisinya lagi di genap
        1 + hitungBiaya(x `div` 2)
    else -- Posisi ganjil
        1 + hitungBiaya(3*x + 1)
