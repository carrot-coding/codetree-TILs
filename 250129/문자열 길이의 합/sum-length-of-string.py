n = int(input())
length = 0
cnt = 0

for i in range(n) :
    input_str = input()
    length += len(input_str)
    if input_str[0] == 'a':
        cnt += 1

print(length, end=' ')
print(cnt)
