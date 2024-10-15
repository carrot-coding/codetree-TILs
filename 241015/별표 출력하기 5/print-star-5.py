n = int(input())
for i in range(n):
    for _ in range(n-i):
        for j in range(n-i):
            print("*", end ='')
        print(end=" ")
    print()