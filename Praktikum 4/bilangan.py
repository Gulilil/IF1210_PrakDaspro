# Nama : Juan Christopher Santoso
# NIM : 16521098
# Deskripsi : Memasukan sejumlah integer kedalam list, lalu mengembalikan apakah ada (serta letak) nilai 0, -1 atau 1

# Kamus :
# n : int
# bilangan : int
# x : int

# Algoritma
n = int(input())
while n <= 0 or n > 100:
    print("Masukan salah. Ulangi!")
    n = int(input())

# Membuat list kosong
angka = []
# Memasukan N buah integer ke dalam list
for i in range(n):
    bilangan = int(input())
    angka.append(bilangan)

#print(angka) # Tidak ditampilkan untuk soal, hanya untuk memantau

# Meminta masukan integer x
x = int(input())

if x == 0:
    if x in angka:
        for i in range(n):
            if angka[i] == x:
                print(i+1)
                break
    else:
        print("Tidak ada 0")
elif x == -1:
    for i in range(n):
        if angka[i] < 0:
            print(i+1, angka[i])
            break
        if i == n-1 : # Jika sampai suku terakhir
            if angka[i] >= 0: # Jika setelah pengecekan, suku terakhir tetap positif atau 0
                print("Tidak ada negatif")

elif x == 1:
    for i in range(n):
        if angka[i] > 0:
            print(i+1, angka[i] )
            break
        if i == n-1: # Jika sampai suku terakhir
            if angka[i] <= 0 :# Setelah pengecekan hingga suku terakhir tetap negatif atau 0
                print("Tidak ada positif")
else:
    print("Tidak diproses")