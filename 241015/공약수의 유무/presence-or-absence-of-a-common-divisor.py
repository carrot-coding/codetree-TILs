inp = input()
arr = inp.split()
a, b = int(arr[0]), int(arr[1])
sat = False
for i in range(a,b+1):
    if (1920 % i == 0) or (2880 % i == 0):
        sat = True
if sat == True :
    print(1)
else:
    print(0)