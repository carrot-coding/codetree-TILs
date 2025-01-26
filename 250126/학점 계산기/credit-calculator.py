n = int(input()) #과목수
arr = input().split() #과목 학점 입력
sum_val = 0
for i in range(n):
    sum_val += float(arr[i])
    total = sum_val/n
print(f"{total:.1f}")
if total >= 4.0:
    print("Perfect")
elif total >= 3.0:
    print("Good")
else :
    print("Poor")