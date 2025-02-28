a, b, c, d = map(int, input().split())
hour = c - a
minute = 0

if d > b :
    minute = d - b
else :
    hour = hour - 1
    minute = (60+d) - b

total = hour * 60 + minute
print(total)
