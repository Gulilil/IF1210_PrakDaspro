n = int(input())
c1 = input()[0]
c2 = input()[0]


if n <= 0 :
    print("Masukan tidak valid");
elif c1 == c2 :
    print("Masukan tidak valid");
else:
    for i in range (n):
        for j in range (n):
            if i == 0 or i == (n-1):
                print(c1, end='');
            elif j == 0 or j == (n-1):
                print(c1, end='');
            else :
                print(c2, end='');
        print("");





'''
else:
    for i in range (n):
        for j in range (n):
            if j == (n-1) and i == (n-1) :
                print(c1)
            elif j == (n-1):
                print(c1, end='\n');
            elif i == 0 or i == (n-1) or j == 0:
                print(c1, end='');
            else :
                print(c2, end='');
        print("");
'''


