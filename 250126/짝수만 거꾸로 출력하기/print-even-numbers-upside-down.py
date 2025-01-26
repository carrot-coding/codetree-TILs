n = int(input())
arr = list(map(int, input().split()))
list = []
for elem in arr:
    if elem % 2 == 0:
        list.append(elem)
for j in list[::-1]:
    print(j, end=' ')    