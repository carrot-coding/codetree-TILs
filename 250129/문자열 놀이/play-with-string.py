A, B = tuple(input().split())
A = list(A)
B = int(B)
#print(A, B)
for i in range(B) :
    Q = list(input().split())
    #print(Q)
    if int(Q[0]) == 1 :
        a = int(Q[1])
        b = int(Q[2])
        c = A[a - 1]
        d = A[b - 1]
        A[b - 1] = c
        A[a - 1] = d
        print(''.join(A))
    else :
        for i in range(len(A)) :
            if A[i] == Q[1] :
                A[i] = Q[2]
        print(''.join(A))