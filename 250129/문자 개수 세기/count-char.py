str_ = input()
find = input()
cnt = 0

for i in range(len(str_)):
    if str_[i] == find :
        cnt += 1
print(cnt)