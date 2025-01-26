score = input().split()
sum_val = 0
for i in range(8):
    arr = float(score[i])
    sum_val += arr
avg_val = sum_val/8
print(f"{avg_val:.1f}")