module ListOfInteger where

{-
Buatlah fungsi nbElmt yang menerima masukan sebuah
 list of integer (mungkin kosong) dan menghasilkan
  banyaknya elemen dalam list (0 jika list kosong) 
  secara rekursif. Dilarang menggunakan fungsi standar di Haskell (kecuali untuk selektor). 
  -}

nbElmt :: [Int] -> Int
nbElmt l =
    if length l == 0 then -- Basis
        0
    else  -- Rekurens
        1 + nbElmt (tail l)
