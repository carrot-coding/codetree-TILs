binary = list(map(int,input()))
#print(binary)
num = 0

# Write your code here!
for i in binary:
    num = num*2 + i
print(num)