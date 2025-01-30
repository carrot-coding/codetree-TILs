a, b = map(int, input().split())

# Write your code here!
def zegop(a, b) :
    start = 1
    for i in range(b) :
        start = start * a
    print(start)

zegop(a, b)