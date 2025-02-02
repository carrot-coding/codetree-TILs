a, b = map(int, input().split())

# Write your code here!
def funtion(a, b) :
    if a <= b :
        a += 10
        b *= 2
    else :
        b += 10
        a *= 2
    return a, b

#print(funtion(a, b))
for elem in funtion(a, b) :
    print(elem,end=' ')