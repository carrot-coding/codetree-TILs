n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

x, y = 0, 0
for i in range(n) :
    move = dir[i]
    if move == 'N' :
        y += dist[i]
    elif move == 'W' :
        x -= dist[i]
    elif move == 'S' :
        y -= dist[i]
    else :
        x += dist[i]
print(x, y)