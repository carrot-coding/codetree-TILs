A = list(input())
for i in range(len(A)-1) :
    Q = int(input())
    if Q > len(A) :
        A.pop(-1)
        print(''.join(A))
    else :
        A.pop(Q)
        print(''.join(A))
