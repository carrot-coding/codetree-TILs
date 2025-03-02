dirs = input()
a = len(dirs)
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]
x, y = 0, 0
base_dir = 0

for i in range(len(dirs)):
    if dirs[i] == 'L':
        base_dir = (base_dir+3)%4    
    elif dirs[i] == 'R' :
        base_dir = (base_dir+1)%4
    else :
        x += dxs[base_dir]
        y += dys[base_dir]
print(x,y)