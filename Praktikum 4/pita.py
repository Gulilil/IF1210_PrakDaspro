# Nama : Juan Christopher Santoso
# NIM : 16521098
# Deskripsi : Membuat pola pita sesuai dengan n yang diinputkan oleh pengguna. n harus ganjil dan positif

# Kamus :
# n = int

# Prosedur dan Fungsi
# Algoritma:
def IsValid(n):
    if n <= 0 or n % 2 == 0:
        return False
    else:
        return True

def GambarPita(n):
    for i in range (1, n+1):
        tengah = (n+1)/2 # Menentukan baris tengah
        daritengah = abs(tengah-i) # Menghitung jarak baris ke-i terhadap baris tengah
        kosong = (n-1) - 2*daritengah # Semakin jauh dari tengah, semakin sedikit bagian kosong (spasi)
        stghkosong = kosong/2 # Bagian kosong terdapat pada kiri dan kanan, bagian kiri saja adalah setengah kosong
        print(" "*int(stghkosong) + "*"*int(n-kosong))


# Program Utama
n = int(input(""))
if IsValid(n) == False:
    print("Masukan tidak valid")
else:
    GambarPita(n)