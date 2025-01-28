n, q = tuple(map(int, input().split()))
arr_elem = list(map(int, input().split())) #원소 리스트
num = 0
elem = 0

#질문시작
for i in range(q):
    arr = list(map(int, input().split()))
    if arr[0] == 1:
       num = arr[1]
       k = num - 1
       print(arr_elem[k])
    elif arr[0] == 2:
        find = arr[1]
        for elem in arr_elem:
            if find == elem:
                print(arr_elem.index(elem)+1)
                break
    else:        
        a = arr[1]
        b = arr[2]
        for j in range(a-1, b):
            print(arr_elem[j], end=' ')
        print()