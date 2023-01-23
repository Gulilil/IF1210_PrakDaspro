n = int(input())            # asumsi 0 < n <= 100

angkalist = [0 for i in range(n)]
for i in range(n):
    angkalist[i] = int(input())

x = int(input())
available = False           # Apakah x ada pada list

for i in range(n):
    if (i == 0):
        max = angkalist[i]
        min = angkalist[i]
    if (angkalist[i] == x):
        available = True

    if (angkalist[i] >= max):
        max = angkalist[i]
    elif (angkalist[i] <= min):
        min = angkalist[i]

if (available == False):
    print(x, "tidak ada")
else: # available == True
    if (max == x):
        print("maksimum")
    if (min == x):
        print("minimum")
    if (max != x and min != x):
        print("N#A")
