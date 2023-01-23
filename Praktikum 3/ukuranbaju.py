

t = int(input()) # Tinggi badan
b = int(input()) # Berat badan

'''
t <= 150, b bebas --> M (1)
t > 170, 60 < b <= 80 --> XL (3)
150 < t <= 170 , b <= 80 --> L (2)
                , b > 80 --> XL (3)
else --> 4

'''
hasil = 4;
if (t > 170):
    if (b > 60 and b <= 80):
        hasil = 3;
    else :
        hasil = 4;
elif ( t > 150 and t <= 170):
    if (b <=80):
        hasil = 2;
    elif (b > 80):
        hasil = 3;
elif (t <= 150):
    hasil = 1;
else :
    hasil = 4;

print(hasil)