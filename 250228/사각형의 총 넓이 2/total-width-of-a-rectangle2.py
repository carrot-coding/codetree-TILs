n = int(input())
checked = [[0 for _ in range(201)] for i in range(201)]

for _ in range(n):
    a, b, c, d = map(int,input().split())
    a, b, c, d = a+100, b+100, c+100, d+100
    for i in range(a, c):
        for j in range(b, d):
            checked[i][j] += 1
cnt = 0
for i in range(201):
    for j in range(201):
        if checked[i][j] != 0 :
            cnt += 1
print(cnt)