n = int(input())
sum_val = 0
cnt = 0
for i in range(n):
    number = int(input())
    cnt += 1
    sum_val += number
avg = sum_val/cnt
print(f"{sum_val} {avg:.1f}")