n = int(input())
price = list(map(int, input().split()))
cnt = 0

for i in range(n-1) :
    if price[i] > price[i+1] :
        cnt += 1
        if cnt == n-1 :
            print(0)

