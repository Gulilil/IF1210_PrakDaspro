def IsValid(n):
    if n <= 0 or n % 2 == 0:
        return False
    else :
        return True

def GambarBTercermin(n):
    for i in range (1, n+1):
        tengah = (n+1)/2
        daritengah = abs(tengah - i)
        kosong = (n - 1) - 2*daritengah
        print(" "*int(kosong) + "*"*int(n-kosong))

n = int(input(""))
if IsValid(n) == False:
    print("Masukan tidak valid")
else:  # Sudah pasti ganjil (True)
    GambarBTercermin(n)