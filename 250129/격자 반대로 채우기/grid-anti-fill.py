n = int(input())
arr_2d = [[0 for _ in range(n)] for _ in range(n)]
sum_val = n*n

for j in range(n) :
    if n % 2 == 0 : #n이 짝수
        if j % 2 == 0 :        
            for i in range(n) :
                arr_2d[n-1-i][j] = sum_val
                sum_val -= 1
        else :
            for i in range(n) :
                arr_2d[i][j] = sum_val
                sum_val -= 1
    else : #n이 홀수
        if j % 2 != 0 :        
            for i in range(n) :
                arr_2d[n-1-i][j] = sum_val
                sum_val -= 1
        else :
            for i in range(n) :
                arr_2d[i][j] = sum_val
                sum_val -= 1

for row in arr_2d :
    for elem in row :
        print(elem, end=' ')
    print()