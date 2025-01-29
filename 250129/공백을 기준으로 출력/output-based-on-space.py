str1 = input()
str2 = input()
# for i in range(len(str1)):
#     if str1[i] == ' ' :
#         print(i)
# for i in range(len(str2)):
#     if str2[i] == ' ' :
#         print(i)

for elem in str1 :
    if elem != ' ':
        print(elem, end='')
for elem in str2 :
    if elem != ' ':
        print(elem, end='')