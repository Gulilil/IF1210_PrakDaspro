# Program pengurutan list
# Program memiliki sebuah integer yang menjadi penanda dari panjangnya suatu list.
# Lalu, program akan meminta user untuk menginputkan suatu integer untuk semua index pada list tersebut
# Program akan mengurutkan nilai pada list sehingga menjadi mengurut mengecil
'''
Kamus :
    n : int
    angkaList : array of int
    angka : int
    function get_max (array, indexstart) -> int
    function get_idx (array, number) -> int
    function swap (array, index1, index2) -> array of int
    procedure sort (arr) 
'''


def get_max(array, indexstart):
    '''
    Kamus Lokal:
        array : array of int
        indexstart : int
        length : int
        maxVal : int
    '''
    # Mengukur panjang array
    length = 0
    for i in array :
        length +=1
    
    maxVal = array[indexstart]
    for i in range(indexstart, length):
        if (array[i] > maxVal):
            maxVal = array[i]
    
    return maxVal

def get_idx(array, number):
    '''
    Kamus Lokal:
        array : array of int
        number : int
        length, idx : int
    '''
    # Mengukur panjang array
    length = 0
    for i in array :
        length +=1
    
    idx = 0
    for i in range(length):
        if (array[i] == number):
            idx = i

    return idx

def swap(array, indeks1, indeks2):
    '''
    Kamus Lokal:
        array : array of int
        indeks1, indeks2, temp : int
    '''
    temp = array[indeks1]
    array[indeks1] = array [indeks2]
    array[indeks2] = temp

    return array

def sort (arr):
    '''
    Kamus Lokal:
        arr : array of int
        maxArr : int
        maxIdx : int
        function get_max(arr, i) -> int
        function get_idx(arr, maxArr) -> int
        function swap(arr, i, maxIdx) -> array of int
    '''
    for i in range(len(arr)):
        maxArr = get_max(arr,i)
        maxIdx = get_idx(arr, maxArr)
        swap(arr, i, maxIdx)
    print(arr)



n = int(input())

angkaList = [0 for i in range(n)]

for i in range(n):
    angka = int(input())
    angkaList[i] = angka

sort(angkaList)
