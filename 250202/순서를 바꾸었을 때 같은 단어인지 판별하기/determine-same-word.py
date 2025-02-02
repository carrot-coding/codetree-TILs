word1 = input()
word2 = input()

# Write your code here!
word1 = list(word1)
word2 = list(word2)

word1.sort()
word2.sort()

cnt = 0
for i in range(len(word1)):
    for i in range(len(word2)):
        if word1[i] != word2[i] :
            cnt += 1
if cnt > 0 or (len(word1)!=len(word2)):
    print('No')
else:
    print('Yes')