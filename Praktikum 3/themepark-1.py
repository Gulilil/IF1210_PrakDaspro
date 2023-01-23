# Kamus :
# t, b, k = Int

# Algoritma
t = int(input())
b = int(input())
k = int(input())

if t > 100 and b <= 150:
    if k == 1:
        print("FALSE")
    elif k == 2 or k == 3 or k == 4 :
        print("TRUE")
    else :
        print("FALSE")
elif k == 1:
    if t <=100 and b <=150:
        print("TRUE")
    else:
        print("FALSE")
elif k == 2 :
    if t<= 100 and b>30 and b <=150:
        print("TRUE")
    else:
        print("FALSE")
elif b>150:
    if t <=100:
        if k == 2:
            print("TRUE")
        elif k ==1 or k ==3 or k ==4:
            print("FALSE")
        else :
            print("FALSE")
    elif t > 100 and t <= 200:
        if k == 2 and k == 3:
            print("TRUE")
        elif k ==1 or k == 4:
            print("FALSE")
        else:
            print("FALSE")
    else :
        print("FALSE")
else :
    print("FALSE")

'''
elif t <=100 and b <= 150:
    if b <= 30:
        if k == 1:
            print("TRUE")
        elif k == 2 or k == 3 or k == 4:
            print("FALSE")
        else:
            print("FALSE")
    else:
        if k == 1 or k == 2:
            print("TRUE")
        elif k == 3 or k == 4 :
            print("FALSE")
        else :
            print("FALSE")
'''