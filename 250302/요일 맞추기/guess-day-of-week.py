# 변수 선언 및 입력
a, b, c, d = tuple(map(int, input().split()))
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
total_a = 0
total_b = 0

# 차이를 계산합니다.
for i in range(1, a) : 
    total_a += days[i]
total_a += b

for i in range(1, c) : 
    total_b += days[i]
total_b += d

# print(total_a)
# print(total_b)
# print((total_b - total_a)%7)
# if total_a > total_b :
#     print(week[(total_b - total_a)%7])
# else : 
print(week[(total_b - total_a)%7])