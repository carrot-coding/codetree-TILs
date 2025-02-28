n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
checked = [[0 for _ in range(101)] for _ in range(101)]

for element in points :
    for i in range(element[0],element[0]+8):
        for j in range(element[1],element[1]+8):
            checked[i][j] += 1
cnt = 0
for i in range(101):
    for j in range(101):
        if checked[i][j] > 0 :
            cnt += 1
print(cnt)