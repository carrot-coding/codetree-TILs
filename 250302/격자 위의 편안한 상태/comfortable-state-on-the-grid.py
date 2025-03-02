n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]
checked = [[0 for _ in range(n)] for _ in range(n)]
dxs = [1, 0, -1, 0]
dys = [0, -1, 0, 1]

def in_range(x, y):
    return 0<=x<n and 0<=y<n

for i in range(m):
    x = points[i][0]-1
    y = points[i][1]-1
    checked[x][y] += 1
    cnt = 0
    for j in range(4):
        nx = x + dxs[j]
        ny = y + dys[j]
        if in_range(nx,ny) and checked[nx][ny] == 1:
            cnt += 1
    if cnt == 3 :
        print(1)
    else :
        print(0)