cnt = 0

for i in range(10):
    str_input = input()
    if str_input[-1] == 'e':
        print(str_input)
        cnt += 1
if cnt == 0 :
    print('None')