a, o, c = input().split()
a = int(a)
c = int(c)

# Write your code here!
def sachik(a, o, c) :
    if o == '+':
        print(a, o, c, '=', a+c)
    if o == '-':
        print(a, o, c, '=', a-c)
    if o == '/':
        print(a, o, c, '=', a/c)
    if o == '*':
        print(a, o, c, '=', a*c)            
    else :
        print('False')
    
sachik(a,o,c)