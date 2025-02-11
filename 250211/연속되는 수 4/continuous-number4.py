n = int(input())
arr = [int(input()) for _ in range(n)]

cnt = 0
max_cnt = 0

for i in range(n):
    if i>=1 and arr[i]>arr[i-1]:
        cnt += 1
    else:
        cnt = 0
    max_cnt = max(max_cnt, cnt)
print(max_cnt+1)