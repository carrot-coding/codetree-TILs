list = ['apple','banana','grape','blueberry','orange']
input_str = input()
cnt = 0

for i in range(5):
    if list[i][2] == input_str or list[i][3] == input_str :
        print(list[i])
        cnt += 1
print(cnt)
