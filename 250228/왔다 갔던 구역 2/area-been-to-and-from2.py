n = int(input())
arr = [0 for _ in range(2002)]

start = 1000
for i in range(n) :
    a, b = tuple(input().split())
    a = int(a)
    
    if b == 'R' :
        for j in range(start, start+a):
            arr[j] += 1
        start = start+a
    else :
        for j in range(start-a,start):
            arr[j] += 1
        start = start - a
cnt = 0
for i in range(2002) :
    if arr[i] > 1:
        cnt += 1
print(cnt)