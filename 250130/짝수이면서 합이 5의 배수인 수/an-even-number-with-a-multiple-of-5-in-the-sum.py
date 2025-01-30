n = int(input())
def is_magic_number(n):
    degit_10 = n // 10
    return n % 2 == 0 and (degit_10 + n - 10*degit_10) % 5 == 0

if is_magic_number(n) == True :
    print('Yes')
else :
    print('No')