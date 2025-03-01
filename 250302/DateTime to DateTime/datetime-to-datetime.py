a, b, c = tuple(map(int, input().split()))
#print(a, b, c)

cnt = 0
day, hour, minute = 11, 11, 11

if a<=11 and b<=11 and c<=11:
    if (a,b,c) != (11, 11, 11):
        print(-1)
    else :
        print(0)
else:
    while True :
        cnt += 1
        minute += 1

        if minute == 60 :
            minute = 0
            hour += 1
            
            if hour == 24 :
                hour = 0
                day += 1

        if day == a and hour == b and minute == c:
            print(cnt)
            break