n = int(input())
cnt = 0
for i in range(1,n*5):
    if n*i % 5 != 0:
        print(n*i, end=' ')
    elif (n*i % 5 == 0) & (cnt == 0) :
        print(n*i, end=' ')
        cnt += 1
    else:
        print(n*i, end=' ')
        break