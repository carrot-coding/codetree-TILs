arr = list(map(int, input().split()))

max_setting = 0
min_setting = 1000

for elem in arr :
    if elem < 500 and elem > 0 :
        if elem > max_setting :
            max_setting = elem
    print(max_setting, end=' ')
    elif elem > 500 :
        if elem < min_setting :
            min_setting = elem
            print(min_setting)
