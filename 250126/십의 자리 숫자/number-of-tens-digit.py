arr = list(map(int, input().split()))
cnt_arr = [0]*9
for elem in arr :
    decade = elem // 10
    if elem == 0 :
        break
    if decade != 0 :
        cnt_arr[decade-1] += 1
for i in range(9) :
    print(f"{i+1} - {cnt_arr[i]}")