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
# Algoritma

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
    
for i in arraydataSaham:
    print(i[0]+","+i[1]+","+str(i[2]))