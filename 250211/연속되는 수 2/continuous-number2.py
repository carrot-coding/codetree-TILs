n = int(input())
arr = [int(input()) for _ in range(n)]
cnt = 0
max_cnt = 0

for i in range(n):
    if i==0 or arr[i-1] != arr[i]:
        cnt = 0
    else :
        cnt += 1
        max_cnt = max(max_cnt,cnt)
print(max_cnt+1)