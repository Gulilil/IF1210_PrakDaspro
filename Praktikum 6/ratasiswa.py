import tulisdata


# Algoritma

def insertionSort(array, index):
    
    # Menukar data bila argumen Id Pemilik lebih lebih kecil dari index sebelumnya
    while (index >=1 and (array[index][0] < array[index-1][0])):
        temp = array[index]
        array[index] = array[index-1]
        array[index-1] = temp
        index = index -1
        
    return array
    '''
    length = 0
    for i in array :
        length +=1
    
    if (length > 1) :
        for i in range (length-1, 0, -1):
            temp = array[i]
            index = i -1
            while (temp[0] < array[index][0] and index > 0) :
                array[index+1] = array[index]
                index = index -1
            if (temp[0] >= array[index][0]) :
                array[index+1] = temp
            else:
                array[index+1] = array[index]
                array[index] = temp
        '''


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
tulisdata.TulisDataSiswa(namafile)
mark = "99999999"


data = open(namafile)

rows = [row.rstrip() for row in data.readlines()]
#print(rows)                                # Hanya untuk pengetesan

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

    #print(arraydataSiswa)                  # Hanya untuk pengetesan
    
    

    arraydataSiswa = arraydataSiswa + [(mark, mark, mark)]      # Penambahan mark pada data array

    calculateMean(arraydataSiswa)

data.close()


    
