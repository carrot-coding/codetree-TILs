n = int(input())

# Write your code here!
def print_reck(n) :
    cnt = 1
    for i in range(n) :
        for i in range(n) :
            print(cnt, end =' ')
            cnt += 1
            if cnt == 10 :
                cnt = 1
        print()

print_reck(n)