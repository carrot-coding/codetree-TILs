n = int(input())
for i in range(2*n):
    if i % 2 == 0:
        for j in range(i//2+1):
            print("*", end=' ')
    else:
        for j in range(n-(i-1)//2):
            print("*",end=' ')
    print()