a = input().split()
b = input().split()
c = input().split()

cnt_a, cnt_b, cnt_c, cnt_d = 0, 0, 0, 0
for _ in (a,b,c):
    if _[0] == 'Y' and int(_[1])>=37 :
        cnt_a += 1
    elif _[0] == 'N' and int(_[1])>=37 :
        cnt_b += 1
    elif _[0] == 'Y' and int(_[1])<37 :
        cnt_c += 1
    else :
        cnt_d += 1

print(cnt_a, cnt_b, cnt_c, cnt_d, end=' ')
if cnt_a >= 2:
    print('E')