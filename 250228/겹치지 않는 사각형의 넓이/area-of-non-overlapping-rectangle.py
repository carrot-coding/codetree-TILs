checked = [[0 for _ in range(2001)] for i in range(2001)]

for _ in range(2):
    a, b, c, d = map(int,input().split())
    a, b, c, d = a+1000, b+1000, c+1000, d+1000
    for i in range(a, c):
        for j in range(b, d):
            checked[i][j] += 1

for _ in range(1):
    a, b, c, d = map(int,input().split())
    a, b, c, d = a+1000, b+1000, c+1000, d+1000
    for i in range(a, c):
        for j in range(b, d):
            checked[i][j] -= 1

cnt = 0
for i in range(2001):
    for j in range(2001):
        if checked[i][j] == 1 :
            cnt += 1
print(cnt)