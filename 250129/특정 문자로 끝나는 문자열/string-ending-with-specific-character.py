cnt = 0
str_input = []

for i in range(10):
    str_ = input()
    str_input.append(str_)

a = input()

for i in range(10) :
    if str_input[i][-1] == a :
        print(str_input[i])
        cnt += 1
if cnt == 0 :
    print('None')