n, m = map(int, input().split())
checked = [[0 for _ in range(m)] for _ in range(n)]
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]
current_dir = 0
x, y = 0, 0
checked[0][0] = 1
def in_range(x,y):
    return 0<=x<n and 0<=y<m

for i in range(2, n*m+1):
    nx = x + dxs[current_dir] 
    ny = y + dys[current_dir]
    if not in_range(nx,ny) or checked[nx][ny] != 0:
        current_dir = (current_dir+1)%4
    nx = x + dxs[current_dir] 
    ny = y + dys[current_dir]
    x, y = nx, ny
    checked[x][y] = i

#print(checked)
for i in range(n):
    for j in range(m):
        print(checked[i][j], end=' ')
    print()