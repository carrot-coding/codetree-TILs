n = int(input())
if n%2 == 0:
    if n == 4 or n== 6:
        print(30)
    elif n == 2 :
        print(28)
    else:
        print(31)
else:
    if n < 8:
        print(31)
    else:
        print(30)