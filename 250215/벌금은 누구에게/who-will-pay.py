N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]
arr = [0 for _ in range(N+1)]
K__ = []
X__ = []
# Write your code here!
ans = -1

for i in student :
    arr[i] += 1
#print(arr)

for i in range(len(arr)) :
    if arr[i] >= K :
        K__.append(i)
#print(K__)

if len(K__) == 0 :
    print(-1)
elif len(K__) == 1 :
    for i in K__ :
        print(i)
else :
    for element in K__ :
        for i in range(len(student)):
            if element == student[i] :
                ans = i
        X__.append(i)
    min = N
    for i in range(X__) :
        if X__[i] < min :
            min = i
    print(K__[min]) 