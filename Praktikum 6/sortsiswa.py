import tulisdata

def insertionSort(array, index):
    # Menukar data bila argumen Id Pemilik lebih lebih kecil dari index sebelumnya
    while (index >=1 and (array[index][0] < array[index-1][0])):
        temp = array[index]
        array[index] = array[index-1]
        array[index-1] = temp
        index = index -1
    return array

namafile = input()
tulisdata.TulisDataSiswa(namafile)
mark = "99999999"

data = open(namafile)
rows = [row.rstrip() for row in data.readlines()]

if rows[0] == mark:
    print("File kosong")
else:
    # Mengukur panjang 
    length = 0
    for i in rows:
        length +=1

    amountdataSiswa = (length-1)//3
    arraydataSiswa = [0 for i in range(amountdataSiswa)]

    for i in range(amountdataSiswa):
        dataSiswa = (rows[i*3], rows[i*3+1], rows[i*3+2])
        arraydataSiswa[i] = dataSiswa
        arraydataSiswa = insertionSort(arraydataSiswa, i)
    
for i in arraydataSiswa:
    print(i[0]+","+i[1]+","+str(i[2]))