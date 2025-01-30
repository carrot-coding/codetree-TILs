y = int(input())

def yun_neon(y) :
    if y % 100 == 0 and y % 400 != 0 :
        return False
    if y % 4 == 0 :
        return True
    return False

def deter(y) :
    if yun_neon(y) :
        print('true')
    else:
        print('false')
deter(y)