str_input = input()
n = int(input())

if len(str_input) > n :
    for i in range(-1,-n-1,-1) :
        print(str_input[i], end='')
else :
    for i in range(-1,-len(str_input)-1,-1) :
        print(str_input[i], end='')