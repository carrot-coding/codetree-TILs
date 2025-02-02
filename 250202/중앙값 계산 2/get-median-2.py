n = int(input())
arr = list(map(int, input().split()))

# Write your code here!
arr.sort()
for i in range(1,n+1,2):
    print(arr[(i+1)//2-1],end=' ')