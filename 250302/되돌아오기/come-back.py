N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]
x, y, direction = 0, 0, 0
dxs = [1,0,-1,0]
dys = [0,-1,0,1]
dirs = ['E','S','W','N']
cnt = 0

for i in range(N):
    direction = dirs.index(dir[i])
    for j in range(dist[i]):
        cnt += 1
        x = x + dxs[direction]
        y = y + dys[direction]
        if x == 0 and y == 0 :
            print(cnt)
            break
