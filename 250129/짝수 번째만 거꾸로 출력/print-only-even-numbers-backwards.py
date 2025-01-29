A = input()
length = len(A)

if length % 2 == 0 :
    for i in range(-1,-length-1,-2):
        print(A[i], end='')
else :
    for i in range(-2,-length-1,-2):
        print(A[i], end='')


