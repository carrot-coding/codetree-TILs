arr_2d = [list(map(int, input().split())) for i in range(3)]
delete_ = input()
arr_2d_2 = [list(map(int, input().split())) for j in range(3)]
#print(arr_2d)
#print(arr_2d_2)

for i in range(3) :
    for j in range(3) :
        a= arr_2d[i][j]
        b= arr_2d_2[i][j]
        print(a*b, end=' ')
    print()