n = int(input())

checked = [list(map(int,input().split())) for _ in range(n)]

def in_range(x, y):
    return 0<= x <n and 0<= y <n
total_cnt = 0

for i in range(n):
    for j in range(n):
        cnt = 0
        if in_range(i-1,j) and checked[i-1][j] == 1 :
            cnt += 1
        if in_range(i,j-1) and checked[i][j-1] == 1 :
            cnt += 1
        if in_range(i+1,j) and checked[i+1][j] == 1 :
            cnt += 1
        if in_range(i,j+1) and checked[i][j+1] == 1 :
            cnt += 1
        if cnt >= 3 :
            total_cnt += 1
print(total_cnt)