arr = list(map(int, input().split()))
arr_2d =[]
for _ in range(4):
    arr_2d.append(arr)
for i in range(4) :
    for j in range(4) :
        if i >= j :
            sum_val += arr_2d[i][j]

print(sum_val)