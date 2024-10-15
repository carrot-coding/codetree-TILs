inp = input()
arr = inp.split()
a, b, c = int(arr[0]), int(arr[1]), int(inp[2])
sat = False
for i in range(a, b+1):
    if i % c == 0:
        sat = True
if sat == True:
    print("YES")
else :
    print("NO")