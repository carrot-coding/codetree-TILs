n = int(input())
A = list(map(int, input().split()))
B = [0 for _ in range(n)]
A.sort()
for i in range(n) :
    B[i] = A[i] + A[2*n-i-1]
b = max(B)
print(b)
# Write your code here!
