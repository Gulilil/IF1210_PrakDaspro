

berat = int(input())



if (berat != -999):
    berat50 = 0
    berat100 = 0
    mahasiswa = 0
    sum = 0

    while (berat != -999):
        if (30 <= berat <=200):
            sum = sum + berat
            mahasiswa = mahasiswa + 1
            if (berat <= 50):
                berat50 +=1
            elif (berat >=100):
                berat100 +=1
            
        berat = int(input())

    if (mahasiswa > 0):
        print(mahasiswa)
        print(berat50)
        print(berat100)
        rata = round(sum/mahasiswa)
        print(rata)
    else: # Tidak ada data valid
        print("Data kosong")

else:
    print("Data kosong")

