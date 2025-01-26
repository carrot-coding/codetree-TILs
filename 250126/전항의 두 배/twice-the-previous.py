arr = list(map(int, input().split()))
cnt = 1
for i in range(8):
    arr.append(arr[cnt]+2*arr[cnt-1])
    cnt += 1
for elem in arr:
    print(elem, end=' ')