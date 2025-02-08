a, b = map(int, input().split())
n = list(map(int,input()))
#print(n)
# Write your code here!
num = 0

for i in n :
    num = num*a + i

arr = []

while True :
    if num < b :
        arr.append(num)
        break
    arr.append(num%b)
    num = num // b

for i in arr[::-1]:
    print(i, end='')