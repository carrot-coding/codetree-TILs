n, t = map(int, input().split())
arr = list(map(int, input().split()))
cnt, max_cnt = 0, 0

# Write your code here!
for i in range(n):
    if arr[i] > t:
        cnt += 1
    else :
        cnt = 0
    max_cnt = max(max_cnt, cnt)
print(max_cnt)