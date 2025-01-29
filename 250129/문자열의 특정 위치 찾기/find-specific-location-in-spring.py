A, B = tuple(input().split())
str_idx = -1
length = len(A)
for i in range(length):
    if A[i] == B :
        str_idx = i
        print(str_idx)
        break
if str_idx == -1 :
    print("No")
