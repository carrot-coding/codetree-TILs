n = int(input())
arr = [tuple(map(int,input().split())) for _ in range(n)]

zero_base = 100
base = [0 for _ in range(201)]

for tuple in arr :
    for i in range(tuple[0]+100, tuple[1]+100) :
        base[i] += 1

print(max(base))