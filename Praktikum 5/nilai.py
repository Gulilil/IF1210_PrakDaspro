nilai = int(input())

if (nilai != -9999):
    kurang40 = 0
    lebih40 = 0
    sum = 0
    total = 0
    while(nilai != -9999):
        if (0 <= nilai <= 100):
            total +=1
            sum = sum + nilai
            if (nilai >=40):
                lebih40 +=1
            else :
                kurang40 +=1

        nilai = int(input())
    
    if (total == 0):
        print(total)
    else:
        print(total)
        print(lebih40)
        print(kurang40)
        rata = sum/total
        print("{:.2f}".format(rata))

else :
    print("Data nilai kosong")