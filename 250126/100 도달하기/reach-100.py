b = int(input())
a = 1
arr = []

arr.append(a)
arr.append(b)
cnt = 1

while True:
    cnt += 1
    arr.append(arr[cnt-1]+arr[cnt-2])
    if arr[cnt]>= 100:
        break

for elem in arr:
    print(elem,end=' ')