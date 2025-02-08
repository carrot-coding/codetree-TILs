N = list(map(int, input()))
num = 0
# Write your code here!
for i in N:
    num = num*2 + i

num = num*17
num_list = []

while True :
    if num < 2 :
        num_list.append(num)
        break
    num_list.append(num%2)
    num = num // 2

for i in num_list[::-1]:
    print(i,end='')