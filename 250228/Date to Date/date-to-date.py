m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.

days_to_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
cnt = 1

while True :
    if m1 == m2 and d1 == d2:
        break

    d1 += 1
    cnt += 1
    
    if d1 > days_to_month[m1] :
        m1 += 1
        d1 = 1

print(cnt)