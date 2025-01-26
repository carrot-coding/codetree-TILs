arr = list(map(int, input().split()))
for elem in arr :
    if elem % 3 == 0:
        i = arr.index(elem)
        print(arr[i-1])
        break