module SumKelipatanX where

sumKelipatanX :: Int -> Int -> Int -> Int 

sumKelipatanX m n x =
    let batas =  if (m `div` x)*x == m then m 
        else 
            x*((m `div` x)+1)
    in
        if m > n then -- Basis
        0
        else -- Rekurens
        batas + sumKelipatanX (batas+x) n x