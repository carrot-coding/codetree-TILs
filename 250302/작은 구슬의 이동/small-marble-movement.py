n, t = tuple(map(int,input().split()))
a, b, d = tuple(input().split())
a, b = int(a), int(b)
a, b = a-1, b-1
directions = ['U','R','D','L']
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]
dir = 0

def in_range(x):
    return 0<=x<n

for i in range(4) :
    if d == directions[i]:
        dir = i
print(dir)
print(dxs[dir])
for i in range(t) :
    a = a + dxs[dir]
    b = b + dys[dir]
    if not in_range(a):
        a = a - dxs[dir]
        dir = abs(4-a)
    if not in_range(b):
        b = b - dys[dir]
        dir = abs(2-b)