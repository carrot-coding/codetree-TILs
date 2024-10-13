inp = input()
arr = inp.split()
a = float(arr[0])
b = float(arr[1])
if a, b >= 1.0:
    print("High")
elif a, b >= 0.5:
    print('Middle')
else:
    print("Low")