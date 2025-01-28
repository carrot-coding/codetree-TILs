n = int(input())
arr = list(map(int, input().split()))
index_for_max = n

while index_for_max != 0:
    for elem in arr[:index_for_max] :
        max_val = 0
        if elem > max_val :
            max_val = elem
    #print(max_val)
    index_for_max = arr.index(max_val)
    print(index_for_max + 1, end=' ')
