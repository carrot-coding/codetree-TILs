n = int(input())
arr = list(map(int, input().split()))
min_diff = 99
for i in range(n) :
    for j in range(n) :
        diff = arr[i] - arr[j]
        if diff < min_diff and diff > 0 :
            min_diff = diff
print(min_diff)


        # 차이가 0보다 커야함