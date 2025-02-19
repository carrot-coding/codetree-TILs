n = int(input())
a = [
    list(map(int, input().split()))
    for _ in range(n)
]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

def in_range(x,y) :
    return x >= 0 and x < n and y >= 0 and y < n

cnt_more_than_3 = 0

for i in range(n) :
    for j in range(n) :
        cnt = 0
        for k in range(4) :
            x = i + dx[k]
            y = j + dy[k]
            if in_range(x,y) and a[x][y] == 1 :
                cnt += 1
        if cnt >= 3 :
            cnt_more_than_3 += 1

print(cnt_more_than_3)