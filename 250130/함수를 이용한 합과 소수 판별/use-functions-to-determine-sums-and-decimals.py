a, b = map(int, input().split())
def even_number(n) :
    if n >= 10 :
        a = n // 10
        b = n % 10
        if (a + b) % 2 == 0 :
            return True
        else : 
            return False
    else :
        if n % 2 == 0 :
            return True
        else :
            return False
    
def prime_number(n) :
    for i in range(2, n) :
        if n % i == 0 :
            return False
        else :
            return True

def fandan(a, b) :
    cnt = 0
    for i in range(a, b + 1) :
        if even_number(i) :
            if prime_number(i) :
                cnt += 1
    print(cnt)

fandan(a, b)