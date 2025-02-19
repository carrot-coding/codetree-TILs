n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)  # 1-indexed 유지

dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]
mapper = {'R': 0, 'D': 1, 'U': 2, 'L': 3}

dir_num = mapper[d]

# in_range 함수 정의 (1-indexed 방식)
def in_range(x, y):
    return 1 <= x <= n and 1 <= y <= n  # 1부터 N까지 유효

for _ in range(t):
    # 먼저 이동을 시도
    nx, ny = r + dxs[dir_num], c + dys[dir_num]

    # 이동한 곳이 범위를 벗어나면 방향을 반대로 바꾸고, 이동 취소
    if not in_range(nx, ny):
        dir_num = 3 - dir_num  # 방향 전환
    else:
        r, c = nx, ny  # 범위 안이면 이동 확정

# 최종 좌표 출력 (1-indexed 그대로)
print(r, c)
