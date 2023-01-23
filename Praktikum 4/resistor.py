# Nama : Juan Christopher Santoso
# NIM : 16521098
# Deskripsi : Menghitung nilai resistor ekuivalen dengan hubungan Seri atau Paralel

# Kamus :
# r1, r2, r3 : float
# hubungan : string
# seri, paralel : float

# Algoritma :
r1 = float(input(""))
r2 = float(input(""))
r3 = float(input(""))
hubungan = input("")[0].upper()


while r1 <= 0 or r2 <= 0 or r3 <= 0 or (hubungan != "P" and hubungan != "S"):
    print("Masukan salah")
    r1 = float(input(""))
    r2 = float(input(""))
    r3 = float(input(""))
    hubungan = input("")[0].upper()

if hubungan == "S":
    seri  = r1+r2+r3
    print("{:.2f}".format(seri))
else:
    paralel = r1*r2*r3 / (r1*r2 + r2*r3 + r3*r1)
    print("{:.2f}".format(paralel))