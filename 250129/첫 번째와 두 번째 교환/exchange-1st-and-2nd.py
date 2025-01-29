A = list(input())
a = A[0]
b = A[1]

for i in range(len(A)):
    if A[i] == a :
        A[i] = b
    elif A[i] == b :
        A[i] = a

#print(A)
for elem in A :
    print(elem, end='')