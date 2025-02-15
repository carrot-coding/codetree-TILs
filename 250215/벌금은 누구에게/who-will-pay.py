N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# Write your code here!
ans = -1
for i in range(len(student)) :
    for j in range(i+1, len(student)) :
        if student[i] == student[j] :
            ans = student[i]
            break
print(ans)