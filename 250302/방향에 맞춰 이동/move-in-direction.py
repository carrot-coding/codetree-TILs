n = int(input())
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
direction = ['E','S','W','N']
x, y = 0, 0

for _ in range(n):
    a, b = tuple(input().split())
    b = int(b)
    for i in range(4):
        if a == direction[i] :
            for _ in range(b):
                x += dx[i]
                y += dy[i]
print(x, y)