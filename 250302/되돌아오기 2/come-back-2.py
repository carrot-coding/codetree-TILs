commands = input()
directions = ['F','R','L']
dxs = [1,0,-1,0]
dys = [0,-1,0,1]
dir_num = 3
x, y, cnt = 0, 0, 0
max_cnt = -1
for i in range(len(commands)):
    if commands[i] == 'F':
        x = x + dxs[dir_num]
        y = y + dys[dir_num]
    elif commands[i] == 'R':
        dir_num = (dir_num+1)%4
    else :
        dir_num = (dir_num+3)%4
    cnt += 1
    if (x, y) == (0,0) :
        max_cnt = cnt
        break
print(max_cnt)
