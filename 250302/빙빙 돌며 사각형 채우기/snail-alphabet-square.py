n, m = map(int, input().split())
checked = [[""] * m for _ in range(n)]  # 빈 문자열 배열로 초기화
dxs = [0, 1, 0, -1]  # 동, 남, 서, 북
dys = [1, 0, -1, 0]
current_dir = 0  # 초기 방향: 동쪽
x, y = 0, 0
checked[0][0] = 'A'  # 첫 번째 칸

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

for i in range(2, n * m + 1):
    nx, ny = x + dxs[current_dir], y + dys[current_dir]
    
    # 경계를 벗어나거나 이미 방문한 경우 방향 전환
    if not in_range(nx, ny) or checked[nx][ny] != "":
        current_dir = (current_dir + 1) % 4
        nx, ny = x + dxs[current_dir], y + dys[current_dir]  # 새 방향으로 재계산
    
    # 이동 및 알파벳 저장
    x, y = nx, ny
    checked[x][y] = chr(ord('A') + (i - 1) % 26)  # A~Z 반복

# 출력
for row in checked:
    print(" ".join(row))
