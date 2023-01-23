def IsValid(n):
    if n <= 0 or n % 2 == 0:
        return False
    else :
        return True

def GambarBelahKetupat(n):
        for i in range(1 , n+1):
            tengah = (n+1)/2
            daritengah = abs(tengah-i)
            kosong = 2*daritengah
            stghkosong = kosong/2
            print(" "*int(stghkosong) + "*"*int(n-kosong))


n = int(input(""))
if IsValid(n) == False:
    print("Masukan tidak valid")
else:
    GambarBelahKetupat(n)

