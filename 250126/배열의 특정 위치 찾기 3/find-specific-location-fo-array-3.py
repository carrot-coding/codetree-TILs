arr = list(map(int, input().split()))
cnt = 0

for elem in arr :
    if elem == 0 :
        #print(cnt)
        break
    else:
        cnt += 1
print(sum(arr[cnt-3:cnt]))