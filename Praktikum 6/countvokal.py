# Progrma Hitung Vokal
# Membaca masukan sejumlah karakter yang disimpan dalam file data.txt
# Mengidentifikasi setiap huruf yang ada pada data tersebut
# Nilai variabel penghitung jumlah akan bertambah bila ditemukan huruf vokal

# Kamus 
'''
    constant mark : char= "."
    constant aplhabet : string = "aiueoAIUEO"
    data : SEQFILE of 
        (*) char : char
        (1) mark 
    char : char
    vokal : int
    prosedur TulisTeks
'''
def TulisTeks():
# Membaca kalimat (kumpulan karakter) diakhiri mark dari keyboard
# dan menyimpannya ke file data.txt
    # KAMUS LOKAL
    # f : SEQFILE of char
    # kalimat
    # ALGORITMA
    f = open("dataku.txt",'w')
    kalimat = input() # Baca sebuah kalimat dari keyboard
                      # diakhiri mark '.'
                      # Kalimat kosong hanya ada mark
    f.write(kalimat)  # Menuliskan kalimat ke file
    f.close()

# Inisasi data dan konstanta
TulisTeks()

data = open("dataku.txt","r")
mark = "."
alphabet = "aiueoAIUEO"

# Pembacaan data
char= data.read(1)
vokal = 0
while(char != mark):
    if (char in alphabet):
        vokal +=1
    char = data.read(1)

data.close()
print(vokal)