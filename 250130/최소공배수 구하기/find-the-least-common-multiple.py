n, m = tuple(map(int, input().split()))

def min_common(n, m) :
    common = 0 #공약수
    for i in range(1, min(n,m)+1) :
        if n % i == 0 and m % i == 0 :
            common = i
    #print(common)
    min__ = (n // common) * (m // common) * common
    print(min__)

min_common(n, m)
