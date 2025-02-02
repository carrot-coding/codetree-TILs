N = int(input())
cnt = 0
# Write your code here!
def f(N) :
    global cnt
    if N==1:
        return cnt
    if N % 2 == 0:
        cnt += 1
        return f(N//2)
    else :
        cnt += 1
        return f(N//3)

print(f(N))