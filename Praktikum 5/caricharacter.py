n = int(input())

while (n <= 0 or n > 100):
    print("Masukan salah. Ulangi!")
    n = int(input())

charlist = [0 for i in range(n)]
for i in range(n):
    charlist[i] = input()[0]


cc = input().lower()[0]
if (cc == 'l'):
    i = 0
    while ( i < n):
        if (ord(charlist[i]) >=65 and ord(charlist[i]) <= 90):
            print(i+1, charlist[i])
            i = n                          # loop diselesaikan
        if (i == n-1 and (ord(charlist[i]) < 65 or ord(charlist[i]) > 90)):
            print("Tidak ada huruf besar")
        i = i+1

elif (cc == 's'):
    i = 0
    while (i < n):
        if (ord(charlist[i]) >= 97 and ord(charlist[i]) <= 122):
            print(i+1, charlist[i])
            i = n
        if (i == n-1 and (ord(charlist[i]) < 97 or ord(charlist[i]) > 122)):
            print("Tidak ada huruf kecil")
        i = i+1

elif (cc == 'x'):
    i = 0
    while(i < n):
        if (ord(charlist[i]) not in range(65,91) and ord(charlist[i]) not in range(97,123)):
            print(i+1, charlist[i])
            i = n
        if (i == n-1 and (ord(charlist[i]) in range(65,91) or ord(charlist[i]) in range(97,123))):
            print("Semua huruf")
        i = i+1

else :
    print("Tidak diproses")


''' Tanpa ASCII
alphabetlower = 'abcdefghijklmnopqrstuvwxyz'
alphabetupper = alphabetlower.upper()
numbers = '1234567890'

if (cc == 's'):
    for i in range(n):
        if (charlist[i] in alphabetlower):
            print((i+1), charlist[i])
            break
        if (i == n-1 and charlist[i] not in alphabetlower):
            print("Tidak ada huruf kecil")

elif (cc == "l"):
    for i in range(n):
        if (charlist[i] in alphabetupper):
            print(i+1, charlist[i])
            break
        if (i == n-1 and charlist[i] not in alphabetupper):
            print("Tidak ada huruf besar")

elif (cc == 'x'):
    for i in range(n):
        if (charlist[i] not in alphabetupper and charlist[i] not in alphabetlower):
            print(i+1, charlist[i])
            break
        if (i == n-1 and charlist[i] in (alphabetupper or alphabetlower)):
            print("Semua huruf")
    
else :
    print("Tidak diproses")

'''