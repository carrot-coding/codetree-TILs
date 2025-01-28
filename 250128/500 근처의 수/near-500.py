arr = list(map(int, input().split()))

max_setting = 0
min_setting = 1000

for elem in arr :
    if elem < 500 and elem > 0 and elem > max_setting :
        max_setting = elem
    if elem > 500 and elem < min_setting :
        min_setting = elem
print(max_setting, end=' ')
print(min_setting)
