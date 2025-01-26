arr = list(map(int, input().split()))
for elem in arr :
    if elem == 0:
        a = arr.index(elem)
for elem in arr[0:a] :
    if elem % 2 != 0:
        print(elem+3, end=' ')
    else:
        print(f"{elem/2:.0f}", end=' ')