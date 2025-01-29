A = list(input())
a = A[1]
b = A[0]
for i in range(len(A)) :
    if A[i] == a :
        A[i] = b
print(''.join(A))