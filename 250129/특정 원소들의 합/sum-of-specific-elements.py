arr_2d = []
sum_val = 0

for _ in range(4):
    arr = list(map(int, input().split()))
    arr_2d.append(arr)
print(arr_2d)
for i in range(4) :
    for j in range(4) :
        if i > j or i == j :
            sum_val += arr_2d[i][j]
print(sum_val)
