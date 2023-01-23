segitigalist = [0,0]
userinput = input()

# mengukur panjang kata
length = 0
for i in userinput:
    length +=1

# membuat fungsi pemisah dengan spasi
kata = ""
for i in range (length):
    if (userinput[i] == " "):
        segitigalist[0] = kata
        kata = ""
    elif (i == length-1):
        kata = kata+userinput[i]
        segitigalist[1] = kata
        kata = ""
    else :
        kata = kata+userinput[i]

alas = int(segitigalist[0])
tinggi = int(segitigalist[1])

if (alas <= 0 or tinggi <=0):
    print("Alas dan tinggi harus > 0")
else:
    print(round(1/2*alas*tinggi))