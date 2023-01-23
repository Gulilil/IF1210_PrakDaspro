# Kamus :
# t, b, k = Int

# Algoritma
t = int(input())
b = int(input())
k = int(input())

test = False
#Diset awalnya salah, bila ternyata ada yang benar di tengah jalan, nanti akan berubah jadi benar

if t > 100 and b <=150:
    if k == 1:
        test = False
    elif k ==2 or k == 3 or k ==4 :
        test = True
elif t <=100 and b <= 150:
    if b <= 30:
        if k == 1:
            test = True
        elif k == 2 or k == 3 or k == 4:
            test = False
    else:
        if k == 1 or k == 2:
            test = True
        elif k == 3 or k == 4 :
            test = False
elif b > 150 :
    if t <= 100 :
        if k == 2 :
            test = True
        elif k == 1 or k == 3 or k ==4 :
            test = False
    elif t > 100 and t <=200 :
        if k == 2 or k == 3:
            test = True
        elif k == 1 or k == 4:
            test = False
    else:
        test = False

# Jika sampai akhir tetap salah, brarti tidak termasuk kemana-mana, maka jika 0, dia akan TRUE (karena 0 menandakan kalo dia False semua)
else :
    if k == 0 :
        test = True
    elif k != 0 :
        test = False


if test == False:
    print("FALSE")
else:
    print("TRUE")



'''
if k == 0:
    if test == False and k == 0 :
        print("TRUE")
    elif test == True and k == 0 :
        print("FALSE")
else :
    if test == False :
        print("FALSE")
    else :
        print("TRUE")
'''