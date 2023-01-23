module LuasTrapesium where

-- Menghitung Luas Trapesium                luasTrapesium(a,b,c)

-- Definisi dan Spesifikasi
luasTrapesium :: Float -> Float -> Float -> Float
{- Fungsi luasTrapesium memiliki 3 jenis input yang bertipe float. 3 Input tersebut
merepresentasikan tinggi, dan dua sisi sejajar trapesium. Fungsi tersebut juga memiliki output
bertipe Float yang merupakan luas trapesium berdasarkan data input.-}

-- Realisasi
luasTrapesium a b c = a*(b+c)/2

-- Aplikasi
-- luasTrapesium 2 4 3 = 7.0