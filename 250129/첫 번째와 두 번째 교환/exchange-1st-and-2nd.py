A = list(input())
for i in range(3, len(A)):
    if A[i] == A[0] :
        A[i] = A[1]
    elif A[i] == A[1] :
        A[i] = A[0]
#print(A)
for elem in A :
    print(elem, end='')