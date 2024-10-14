n = int(input())
cnt_class = 0
cnt_corridor = 0
cnt_wc = 0

for i in range(1,n+1):
    if (i % 12 == 0) and (i//12 > 0):
        cnt_wc += 1
    elif i % 3 == 0 and (i//3 > 0):
        cnt_corridor += 1
    elif i % 2 == 0 and (i//2 > 0):
        cnt_class += 1
print(cnt_class, cnt_corridor, cnt_wc)