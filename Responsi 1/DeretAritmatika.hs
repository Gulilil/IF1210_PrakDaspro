module DeretAritmatika where

-- Definisi dan Spesifikasi
deretAritmatika :: Int -> Int -> Int -> Float

-- Realisasi
deretAritmatika n a b = fromIntegral ((n) * (2*a + (n-1)*b))/2

-- fromIntegral ngubah dari Int ke Float