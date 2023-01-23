
import tulisdata

#Kamus:
'''
    type dataSaham : tuple =  (IdPemilik: integer,
                                IdPT: string,
                                Nilai : integer)
    data : SEQFILE of
        (*) row : dataSaham
        (1) mark
    rows : array of string
    length : int
    amountDataSaham : int
    arrayDataSaham : list of tuple
    fungsi  bubbleSort(array)
    fungsi roundDecimals
    prosedur calculateMean

'''

# Algoritma

def insertionSort(array, index):
    # Menukar data bila argumen Id Pemilik lebih lebih kecil dari index sebelumnya
    while (index >=1 and (array[index][0] < array[index-1][0])):
        temp = array[index]
        array[index] = array[index-1]
        array[index-1] = temp
        index = index -1
    return array


def calculateMean(array):

    index = 0
    # Menghitung rata-rata setiap jenis data yang sama
    while (array[index][0] != mark):
        sum = 0
        amount = 0
        currentID = array[index][0]
        while (array[index][0] == currentID):
            sum = sum + int(array[index][2])
            amount = amount +1
            index = index+1
        #mean = roundDecimals(sum/amount, 2)
        mean = sum/amount
        print(currentID+'='+str("{:.2f}".format(mean,2)))

# Menginput nama file dan isi data file
namafile = input()
tulisdata.TulisDataSaham(namafile)
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

    amountdataSaham = (length-1)//3
    arraydataSaham = [0 for i in range(amountdataSaham)]

    for i in range(amountdataSaham):
        dataSaham = (rows[i*3], rows[i*3+1], rows[i*3+2])
        arraydataSaham[i] = dataSaham
        arraydataSaham = insertionSort(arraydataSaham, i)

    arraydataSaham = arraydataSaham + [(mark, mark, mark)]      # Penambahan mark pada data array

    calculateMean(arraydataSaham)

data.close()


    
