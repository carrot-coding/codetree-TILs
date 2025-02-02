n = int(input())
arr = list(map(int, input().split()))
# Write your code here!
for i in range(1,n+1,2):
    arr_ = arr[:i]
    arr_.sort()
    print(arr_[(i+1)//2-1],end=' ')