inp = input()
arr = inp.split()
h = int(arr[0])
w = int(arr[1])
b = int(10000*w/h**2)
print(b)
if b >= 25:
    print("Obesity")