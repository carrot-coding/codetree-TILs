sum_val = 0
cnt = 0

for _ in range(10):
    i = int(input())
    if (i >= 0) and (i <= 200):
        sum_val += i
        cnt += 1
avg = sum_val/cnt
print(f"{sum_val} {avg:.1f}")