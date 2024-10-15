inp = input()
arr = inp.split()
a, b, c = int(arr[0]), int(arr[1]), int(inp[2])
sat = True

for i in range(a, b+1):
    if i % c == 0:
        sat = False

if sat == True:
    print("YES")
else :
    print("NO")