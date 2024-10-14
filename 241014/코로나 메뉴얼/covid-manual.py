inp = input()
arr = inp.split()
a_cold = (arr[0])
a_temp = int(arr[1])

inp = input()
arr = inp.split()
b_cold = (arr[0])
b_temp = int(arr[1])

inp = input()
arr = inp.split()
c_cold = (arr[0])
c_temp = int(arr[1])

if (a_cold == "Y" and a_temp >= 37):
    if (b_cold == "Y" and b_temp >= 37):
        print('E')
    elif (c_cold == "Y" and c_temp >= 37):
        print('E')
    else:
        print('N')
else:
    if (b_cold == "Y" and b_temp >= 37) and (c_cold == "Y" and c_temp >= 37):
        print('E')
    else:
        print('N')