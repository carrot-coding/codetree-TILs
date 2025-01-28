n = int(input())
arr = list(map(int, input().split()))

max_val = arr[0]
second_max = arr[0]

for elem in arr :
    if elem > max_val :
        max_val = elem

print(max_val, end=' ')
#print(arr.index(max_val))

for elem in arr :
    if arr.index(elem) != arr.index(max_val) and elem > second_max :
        second_max = elem

print(second_max)


