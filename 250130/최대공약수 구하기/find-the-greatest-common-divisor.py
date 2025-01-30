n, m = map(int, input().split())

# Write your code here!
def max_elem(n, m) :
    max_i = 0
    if n > m :
        for i in range(1, m+1) :
            if n % i == 0 and m % i == 0 :
                if max_i < i :
                    max_i = i
    else :
        for i in range(1, n+1) :
            if n % i == 0 and m % i == 0 :
                if max_i < i :
                    max_i = i
    print(max_i)

max_elem(n, m)