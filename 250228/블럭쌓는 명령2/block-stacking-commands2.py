n, k = map(int, input().split())
arr = [0 for _ in range(n+1)]

for i in range(k):
    a, b = tuple(map(int, input().split()))
    if a == b :
        arr[a] += 1
    else :
        for j in range(a,b+1):
            arr[j] += 1

print(max(arr[1:]))