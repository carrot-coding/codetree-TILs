str1 = input()
str2 = input()
str3 = input()

# print(len(str1))
# print(len(str2))
# print(len(str3))

max_len = len(str1)
min_len = len(str1)
if len(str2) >= max_len:
    max_len = len(str2)
if len(str3) >= max_len:
    max_len = len(str3)

if len(str2) <= min_len:
    min_len = len(str2)
if len(str3) <= min_len:
    min_len = len(str3)

print(max_len - min_len)