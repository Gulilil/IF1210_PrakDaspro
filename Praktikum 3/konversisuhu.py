t = float(input())
k = input()[0].upper()

if k == "R":
    hasil = t *4/5
elif k == 'F':
    hasil = (t*9/5) + 32
elif k == 'K':
    hasil =  t + 273.15

print('{:.2f}'.format(hasil)) # <- buat bkin 2 angka dibelakang koma