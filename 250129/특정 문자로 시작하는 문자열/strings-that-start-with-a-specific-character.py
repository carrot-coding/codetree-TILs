n = int(input())
str_input = []
cnt = 0
length = 0

for i in range(n) :
    str_input.append(input())
a = input()

for i in range(n) :
    if str_input[i][0] == a :
        cnt += 1
        length += len(str_input[i])
print(f"{cnt} {length/cnt:.2f}")    