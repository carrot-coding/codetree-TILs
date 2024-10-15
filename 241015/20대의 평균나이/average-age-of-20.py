sum_val = 0
cnt = 0
while True :
    age = int(input())

    if age >= 30:
        break
    
    cnt += 1
    sum_val += age
    
avg = sum_val/cnt
print(f"{avg:.2f}")