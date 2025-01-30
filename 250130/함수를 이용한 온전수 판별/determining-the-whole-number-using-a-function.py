a, b = map(int, input().split())

# Write your code here!
def ques_1(n) :
    if n % 2 == 0:
        return True
    
def ques_2(n) :
    if n % 10 == 5:
        return True

def ques_3(n) :
    if n % 3 == 0 and n % 9 != 0 :
        return True

def onjeon(a, b) :
    num = 0
    for i in range(a, b+1) :
        if not ques_1(i) :
            if not ques_2(i) :
                if not ques_3(i) :
                    num += 1
    print(num)
onjeon(a, b)