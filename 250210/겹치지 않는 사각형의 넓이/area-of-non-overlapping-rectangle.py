OFFSET = 1000
MAX_R = 2000
rects = [
    tuple(map(int, input().split()))
    for _ in range(2)]
checked = [[0] * (MAX_R + 1)
    for _ in range(MAX_R + 1)]
for x1, y1, x2, y2 in rects:
    x1, y1 = x1 + OFFSET, y1 + OFFSET
    x2, y2 = x2 + OFFSET, y2 + OFFSET
    for x in range(x1, x2):
        for y in range(y1, y2):
            checked[x][y] += 1

rects2 = [tuple(map(int, input().split()))]
for x1, y1, x2, y2 in rects2:
    x1, y1 = x1 + OFFSET, y1 + OFFSET
    x2, y2 = x2 + OFFSET, y2 + OFFSET
    for x in range(x1, x2):
        for y in range(y1, y2):
            checked[x][y] -= 1

cnt = 0
for x in range(1,MAX_R) :
    for y in range(1,MAX_R) :
        if checked[x][y] > 0 :
            cnt += 1
print(cnt)
