n = int(input())
arr = list(map(int, input().split()))
cnt = 0

for elem in arr :
    if elem == 2 :
        cnt += 1
        if cnt == 3:
            print(arr.index(elem))
            break
        