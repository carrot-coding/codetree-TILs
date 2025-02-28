n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
checked = [[0 for _ in range(202)] for _ in range(202)]

for element in points :
    a = element[0] + 100
    b = element[1] + 100
    for i in range(a, a+8):
        for j in range(b, b+8):
            checked[i][j] += 1
cnt = 0
for i in range(202):
    for j in range(202):
        if checked[i][j] > 0 :
            cnt += 1
print(cnt)