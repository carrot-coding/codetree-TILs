arr = list(map(int, input().split()))
a = arr[0]
b = arr[1]

while True:
    c = a//b
    d = a % b
    print(d, end=' ')
    if c == 1:
        break
