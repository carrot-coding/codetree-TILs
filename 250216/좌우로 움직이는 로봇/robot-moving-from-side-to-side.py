n, m = map(int, input().split())
location_a = [0] * (500000)
location_b = [0] * (500000)

time_a = 0
for i in range(n):
    v, t = tuple(input().split())
    for i in range(int(v)) :
        location_a[time_a+1] = location_a[time_a] + (1 if t == 'R' else -1)
        time_a += 1

time_b = 0
for i in range(m):
    v, t = tuple(input().split())
    for i in range(int(v)) :
        location_b[time_b+1] = location_b[time_b]  + (1 if t == 'R' else -1)
        time_b += 1

#print(location_a[:10])
#print(location_b[:10])
compare = []
for i in range(1, time_a+1) :
    if location_a[i] == location_b[i] :
        compare.append('0')
    else :
        compare.append('X')
for i in range(1,len(compare)):
    if compare[i] != compare[i-1] and compare[i] == '0' :
        print(i+1, end=' ')        
#print(compare[:20])
# change = 0
# for i in range(len(compare)-1):
#     if compare[i] != compare[i+1] :
#         change += 1

# print(change)