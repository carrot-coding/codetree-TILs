M, D = map(int, input().split())
def exist(M, D) :
    if M <= 12 and M > 0 :
        if M in {1, 3, 5, 7, 8, 10, 12} :
            if 1 <= D <= 31 :
                return True
        elif M == 2 :
            if 1<= D <= 28 :
                return True
        else :
            if 1 <= D <= 30 :
                return True
        
    return False

def ff(M,D):
    if exist(M,D) :
        print('Yes')
    else :
        print('No')

ff(M, D)