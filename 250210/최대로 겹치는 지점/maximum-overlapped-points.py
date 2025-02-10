n = int(input())
arr = [0 for _ in range(101)]
for i in range(n) :
    x, y = tuple(map(int, input().split()))
    #print(x,y)
    for j in range(x,y+1):
        arr[j] += 1

max_ = max(arr)
print(max_)