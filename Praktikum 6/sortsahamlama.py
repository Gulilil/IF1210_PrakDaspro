# Program pembacaan data dan pengurutan pemasukan data

import tulisdata

'''
Kamus :
    dataSaham : tuple   =   (IdPemilik  : string,
                            IdPT        : string,
                            Nilai       : int )
    function insertData(word) -> string
    function insertionSort(array, index) -> array
    constant mark : string = "99999999"
    data : SEQFILE of
        (*) readData : string
        (1) mark
    dataLength : int
    sequenceData : string
    kelompokdata : int
    arrayData : array of dataSaham
    index : int
    IdPemilik, IdPT, Nilai : string

'''
# Membuat suatu fungsi yang dapat menghilangkan "\n"
def insertData(word):
    # Mengukur panjang kata
    length = 0
    for i in word :
        length +=1

    newword = ""
    for i in range(length-1):
        newword = newword + word[i]
    
    return newword

def insertionSort(array, index):
    # Menukar data bila argumen Id Pemilik lebih lebih kecil dari index sebelumnya
    while (index >=1 and (array[index][0] < array[index-1][0])):
        temp = array[index]
        array[index] = array[index-1]
        array[index-1] = temp
        index = index -1
    '''
    # Menukar data bila argumen Nilai lebih besar dari index sebelumnya
    while (index >=1  and (array[index][0] == array[index-1][0]) and (array[index][2] > array[index-1][2])):
        temp = array[index]
        array[index] = array [index-1]
        array[index-1] = temp
        index = index-1
    '''
    return array


# Main Program
mark = "99999999"

namafile = input()
tulisdata.TulisDataSaham(namafile)

# Menghitung jumlah data
data = open("saham.txt","r")
dataLength = 0

readData = data.readline()                          # readData adalah data yang masih memiliki "\n"
sequenceData = insertData(readData)                 # sequenceData adalah data yang "\n" sudah dihapus

while (readData != mark):
    #print(sequenceData, dataLength)
    dataLength +=1
    readData = data.readline()
    sequenceData = insertData(readData)
data.close()

# Membuat array dari banyaknya kelompok data yang ada
kelompokData = dataLength // 3                      # Banyaknay kelompok data, 1 kelompok terdiri dari 3 baris
arrayData = [ 0 for i in range(kelompokData)]


# Membaca Isi Data
data = open("saham.txt","r")
readData = data.readline()
index = 0

if (readData == mark):
    print("File kosong")
else :
    for i in range(kelompokData):
        IdPemilik = insertData(readData)                # mengidentifikasi Id Pemilik
        readData = data.readline() 
        IdPT = insertData(readData)                     # mengidentifikasi IdPT
        readData = data.readline()
        Nilai = int(insertData(readData))                  # mengidentifikasi Nilai
        dataSaham = (IdPemilik, IdPT, Nilai)
        arrayData[index] = dataSaham
        
        # Menjalankan fungsi sortInsertion
        arrayData = insertionSort(arrayData, index)

        # Baca baris baru
        readData = data.readline()
        index = index+1

for i in arrayData:
    print(i[0]+","+i[1]+","+str(i[2]))

        



