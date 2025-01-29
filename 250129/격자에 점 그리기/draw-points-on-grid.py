n, m = tuple(map(int, input().split()))
arr_2d = [[0 for _ in range(n)] for _ in range(n)]
cnt = 1

for i in range(m):
    a, b = tuple(map(int, input().split()))
    arr_2d[a-1][b-1] = cnt
    cnt += 1

for row in arr_2d :
    for elem in row :
        print(elem, end = ' ')
    print()