# Kamus 
# C : string or char
# N : Integer


# Algoritma
C = input()[0]
N = int(input())


print(N*C)

'''
Mohon maaf Kak, Bu, Pak. Saya tidak tahu apakah bapak/ibu/kakak akan melihat file ini atau tidak. Tapi saya sudah mencoba
semua algoritma dibawah ini untuk menjawab soal tersebut dan tetap mendapatkan nilai 10/100. Saya ingin bertanya
apakah jawaban yang diset pada grader merupakan jawaban yang sudah tepat? Atau bisa saja jawaban tersebut terlalu terbatas atau 
memiliki ketentuan khusus yang perlu dijawab sehingga mendapatkan nilai benar? Saya tidak menemukan algoritma yang tepat untuk
menemukan jawaban tersebut, padahal jawaban yang dihasilkan pada algoritma-algoritma dibawah ini umumnya sudah tepat. Terima kasih.
'''
#---------------------------------
'''
print(N*C + '\n', end='')
'''

#------------------------------------
'''
kata = ""

for i in range(N):
    kata = kata +C

print(kata+'\n')
'''

#------------------------------------
'''
kata = ""

for i in range(N):
    kata = kata +C

print(kata)
'''

#-------------------------------------
'''
for i in range(N):
        print(C, end='')
'''
#-------------------------------------
'''
for i in range(N):
    if i == N-1 :
        print(C, end='\n')
    else:
        print(C, end='')
'''
#-------------------------------------
'''
for i in range(N):
    if i == N-1 :
        print(C)
    else:
        print(C, end='')
'''
#-------------------------------------
'''
kata = [C for i in range (N)]

for i in range (len(kata)):
    if i == (len(kata)-1):
        print(kata[i], end='\n')
    else:
        print(kata[i], end='')
'''