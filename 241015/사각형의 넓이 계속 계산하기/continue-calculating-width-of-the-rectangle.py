while True :
    inp = input()
    arr = inp.split()
    w = int(arr[0])
    h = int(arr[1])
    cha = arr[2]

    if cha == 'C':
        print(w*h)
        break
    
    print(w*h)