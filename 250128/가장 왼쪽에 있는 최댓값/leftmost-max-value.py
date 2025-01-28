n = int(input())
arr = list(map(int, input().split()))
index_for_max = n

while True:
    for elem in arr[:index_for_max] :
        max_val = 0
        if elem > max_val :
            max_val = elem
    #print(max_val)
    index_for_max = arr.index(max_val)
    if index_for_max != 0:  
        print(index_for_max + 1, end=' ')
    if index_for_max == 0:
        print(index_for_max + 1, end=' ')
        break

