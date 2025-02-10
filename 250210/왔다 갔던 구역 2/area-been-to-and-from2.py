n = int(input())
x = []
base_1 = 0
base_2 = 0
dir = []
arr = [0 for _ in range(2000)]
for _ in range(n):
    xi, di = input().split()
    xi = int(xi)
    x.append(xi)
    dir.append(di)
    if di == 'R':
        base_2 += xi
    else :
        base_2 -= xi
    #print(base_1,base_2)
    if base_2 > base_1 :
        for j in range(base_1+1000, base_2+1000) :
            arr[j] += 1
    else :
        for j in range(base_2+1000, base_1+1000) :
            arr[j] += 1
    base_1 = base_2    
    #print(arr[990:1010])
cnt = 0
for i in range(2000):
    if arr[i] > 1:
        cnt += 1

print(cnt)