OFFSET = 1000
arr = [[0 for _ in range(2002)] for _ in range(2002)]
i_arr = []
j_arr = []
a, b, c, d = tuple(map(int, input().split()))
x, y, z, h = tuple(map(int, input().split()))

a, b, c, d = a+1000, b+1000, c+1000, d+1000
x, y, z, h = x+1000, y+1000, z+1000, h+1000

for i in range(a,c):
    for j in range(b,d):
        arr[i][j] += 1

for i in range(x,z):
    for j in range(y,h):
        arr[i][j] -= 1

for i in range(2002):
    for j in range(2002):
        if arr[i][j] == 1:
            i_arr.append(i)
            j_arr.append(j)
if len(i_arr)==0 or len(j_arr)==0 :
    print(0)
else:
    square = (max(i_arr) - min(i_arr) + 1) * (max(j_arr) - min(j_arr) + 1)
    print(square)