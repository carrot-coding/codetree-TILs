n = int(input())
A = list(map(int, input().split()))
B = [0 for _ in range(n)]
for i in range(n) :
    B[i] = A[i] + A[i-1]
b = max(B)
print(b)
# Write your code here!
