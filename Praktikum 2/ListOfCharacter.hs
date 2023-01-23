module ListOfCharacter where
{-
Buatlah fungsi konkat yang menerima masukan 2 buah list of character, misalnya lc1 dan lc2, yang masing-masing mungkin kosong, 
dan menghasilkan list baru yang merupakan penggabungan lc1 dengan lc2 (lc1 di awal). -}

konkat :: [Char] -> [Char] -> [Char]

konkat k l =
    if length k == 0 && length l == 0 then -- Basis
        []
    else
        if length k == 0 then
            [head l] ++ konkat k (tail l)
        else
            [head k] ++ konkat (tail k) l