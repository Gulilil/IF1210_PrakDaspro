


ip = float(input())
pot = float(input())

if ip >= 3.5:
    print("4")
elif pot < 1 and ip < 3.5:
    print("1")
elif (pot >= 1 and pot < 5) and ip < 3.5:
    if ip >= 2 :
        print("3")
    else :
        print("2")
else:
    print("0")
    