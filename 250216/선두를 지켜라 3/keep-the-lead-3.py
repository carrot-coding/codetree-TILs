N, M = map(int, input().split())
location_a = [0 for _ in range(1000000)]
location_b = [0 for _ in range(1000000)]

# Process A's movements
v = []
t = []
for _ in range(N):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)
time_a = 0
for i in range(N) :
    for j in range(t[i]) :
        location_a[time_a + 1] = location_a[time_a] + v[i]    
        time_a += 1

# Process B's movements
v2 = []
t2 = []
for _ in range(M):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)
time_b = 0
for i in range(M) :
    for j in range(t2[i]) :
        location_b[time_b + 1] = location_b[time_b] + v[i]    
        time_b += 1
# Write your code here!
#print(location_a[:20])
#print(location_b[:20])

compare_loca = []
for i in range(sum(t2)):
    if location_a[i] == location_b[i] :
        compare_loca.append('same')
    elif location_a[i] > location_b[i] :
        compare_loca.append('a')
    else :
        compare_loca.append('b')
#print(compare_loca[:20])

cnt = 0
for i in range(1,len(compare_loca)):
    if compare_loca[i] != compare_loca[i-1] :
        cnt += 1
print(cnt)