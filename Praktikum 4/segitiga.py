def IsValid(n):
    if n <= 0 or n % 2 == 0:
        return False
    else :
        return True

def GambarSegitiga(n):
    if IsValid(n) == False:
        print("Masukan tidak valid")
    else: # Udah pasti ganjil (True)
        for i in range (1, n+1):
            daritengah = abs((n+1)/2 - i)
            kosong = 2 * daritengah
            baris = " "*int(kosong) + "*"*int(n-kosong)
            print(baris)

                
n = int(input(""))
GambarSegitiga(n)