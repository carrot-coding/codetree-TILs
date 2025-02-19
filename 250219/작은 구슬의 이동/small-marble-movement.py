n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]
mapper = {
    'R': 0,
    'D': 1,
    'U': 2,
    'L': 3
}

dir_num = mapper[d]
def in_range(x, y) :
    return 0 <= x and x < n and 0 <= y and y < n

for _ in range(t) :
    nx, ny = r + dxs[dir_num], c + dys[dir_num]
    if not in_range(nx+1, ny+1) :
        dir_num = 3 - dir_num

print(nx, ny)
