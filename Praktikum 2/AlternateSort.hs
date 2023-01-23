module AlternateSort where

-- Definisi dan Spesifikasi

alternateSort :: [Int] -> [Int]
sortlist :: [Int] -> [Int]
findmin :: [Int] -> Int
{- 
1. Urutkan list tersebut

2. Bagi list menjadi 2 sama besar, misal l1 dan l2. Jika panjang list ganjil, maka l1 akan memiliki 1 elemen lebih banyak dibanding l2

3. Ambil elemen terkecil dari l1, masukkan ke akhir l3.

4. Ambil elemen terbesar dari l2, masukkan ke akhir l3.

5. Ulangi langkah 3 dan 4 sampai kedua list kosong.

-}
--[2,4,1,5,6]
-- Realisasi
findmin l =
    if length l == 1 then -- Basis
        head l
    else -- Rekurens
        if head l < head (tail l) then
            findmin ((tail l) ++ [head l])
        else
            findmin (tail l)

sortlist l =
    if length l == 0 then -- Basis
        []
    else -- Rekurens
        if findmin (l) == head l then -- [1] ++ [6,5,2,4]
            [head l] ++ sortlist (tail l)
        else -- [2,4,1,5,6] --> [4,1,6,5,2] --> [1,6,5,2,4]
            sortlist ( (tail l) ++ [head l])


{- head l == max
 sortList (tail l) ++ [head l]
-}

alternateSort l =
    let list = sortlist l
    in
        if length list == 0 then
            []
        else if length list == 1 then
            [head list]
        else
            [head list] ++ [last list] ++ alternateSort (init (tail list))