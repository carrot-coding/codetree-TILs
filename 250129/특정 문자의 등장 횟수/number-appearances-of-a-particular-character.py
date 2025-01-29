A = input()
num_ee = 0
num_eb = 0

for i in range(len(A)-1) :
    if A[i] == 'e' and A[i+1] == 'e':
        num_ee += 1
print(num_ee, end=' ')
for i in range(len(A)-1) :
    if A[i] == 'e' and A[i+1] == 'b':
        num_eb += 1
print(num_eb, end=' ')

    