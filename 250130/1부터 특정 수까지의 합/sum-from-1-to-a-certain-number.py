n = int(input())

# Write your code here!
def sum_val(n) :
    sum__ = 0
    for i in range(1,n+1) :
        sum__ += i
    print(sum__//10)

sum_val(n)