module NbKelipatanX where

nbKelipatanX :: Int -> Int -> Int -> Int 

nbKelipatanX m n x =
    let batas = if (m `div` x)*x == m then m -- Tetap m apabila m adalah kelipatan dari x
        else -- m bukan kelipatan dari x
            ( m `div` x )*x + x
        -- Contoh 1 --> 1 - 1 +3 -> 3
        --        5 --> 5 - 2 +3 -> 6
    in if m > n then -- Basis
            0
        else -- Rekurens
            1 + nbKelipatanX (batas+x) n x
