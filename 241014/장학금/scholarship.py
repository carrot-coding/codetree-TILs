inp = input()
arr = inp.split()
mid = int(arr[0])
final = int(arr[1])
if mid >= 90:
    if final >= 95:
        print(10)
    elif final >= 90:
        print(5)
    else:
        print(0)
else:
    print(0)