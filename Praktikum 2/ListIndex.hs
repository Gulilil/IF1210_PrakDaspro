module ListIndex where

-- Definisi dan Spesifikasi
listIndex :: [Int] -> (Int -> Char) -> [Char]
nilai :: Int -> Char
{- Fungsi listIndex akan menghasilkan sebuah list of character yang melambangkan nilai-nilai indeks dari suatu list nilai integer.
Misal fungsi f akan mengembalikan nilai B untuk range nilai [70,80], maka nilai 75 akan secara otomatis diubah menjadi 'B' oleh fungsi f. -}

{- Materi fungsi sebagai parameter dari fungsi / High Order function, Jadi masukan dari fungsi ini adalah 2, L dan F, dimana L adalah sebuah List, dan F adalah sebuah Fungsi. 
Misalnya pada contoh di bawah ini, F dimasukkan dengan fungsi nilai (tidak usah diimplementasikan), dan L dimasukkan dengan sebuah array. Sehingga, apabila terjadi perubahan skala nilai, 
hanya perlu membuat implementasi nilai yang baru/bisa dengan fungsi lambda dan memanggil langsung fungsi listIndex tanpa harus mengubah implementasi pada listIndex. -}

-- Realisasi
nilai n =
    if n >= 80 && n <= 100 then
        'A'
    else if n >= 70 then
        'B'
    else if n >= 65 then
        'C'
    else if n >= 55 then
        'D'
    else 
        'E'

listIndex l f =
    if length l == 0 then
        []
    else
        [f (head l)] ++ listIndex (tail l) f