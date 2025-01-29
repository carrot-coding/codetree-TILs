n = int(input())
A = list(input().split())
str_ = ""
for i in range(n) :
    str_ += A[i]
#print(str_)
length = len(str_)
n_ = length // 5
n_2 = length % 5
for i in range(n_) :
    print(str_[5*i:5*i+5])
for i in range(n_2) :
    print(str_[5*n_:])
    
