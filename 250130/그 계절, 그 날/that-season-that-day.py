Y, M, D = map(int, input().split())
def exist(Y, M, D) :
    if M <= 12 and M > 0 :
        if M in {1, 3, 5, 7, 8, 10, 12} :
            if 1 <= D <= 31 :
                return True
        elif M == 2 :
            if (Y % 4 == 0) :
                if Y % 100 == 0 and Y % 400 == 0 :
                    if 1<= D <= 29 :
                        return True
                elif Y % 100 != 0 :
                    if 1<= D <= 29 :
                        return True
                else:
                    if 1<= D <= 28 :
                        return True
            else:
                if 1<= D <= 28 :
                    return True
        else :
            if 1 <= D <= 30 :
                return True
    return False

exist(Y, M, D)

if not exist(Y,M,D):
    print(-1)
else: 
    if M in {3, 4, 5} :
        print('Spring')
    elif M in {6, 7, 8} :
        print('Summer')
    elif M in {9, 10, 11} :
        print('Fall')
    else :
        print('Winter')
