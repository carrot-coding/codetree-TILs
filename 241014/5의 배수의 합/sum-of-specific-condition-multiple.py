inp = input()
arr = inp.split()
a = int(arr[0])
b = int(arr[1])
cnt = 0
sum_val = 0

if a >= b:
    for i in range(b+1,a):
        if i%5 == 0:
            sum_val += i
else:
    for i in range(a+1,b):
        if i%5 == 0:
            sum_val += i  
print(sum_val)