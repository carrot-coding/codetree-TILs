inp = input()
arr = inp.split()
a_age = int(arr[0])
a_sex = arr[1]

inp = input()
arr = inp.split()
b_age = arr[0]
b_sex = arr[1]

if (a_age >= 19 and a_sex == 'M') or (b_age >= 19 and b_sex == 'M'):
    print(1)
else:
    print(0)