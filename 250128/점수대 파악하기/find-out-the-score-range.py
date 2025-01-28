arr = list(map(int, input().split()))
cnt_arr = [0 for i in range(11)]

for elem in arr :
    if elem == 0 :
        break
    if elem < 10 :
        continue    
    cnt_arr[elem // 10] += 1

#print(cnt_arr)

for i in range(10,0,-1):
    print(f"{i*10} - {cnt_arr[i]}")
