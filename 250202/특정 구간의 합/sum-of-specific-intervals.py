n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]
# print(queries[0][0])
# Write your code here!
def test(m) :
    global arr
    global queries
    for i in range(m):
        sum_val = 0
        for j in range(queries[i][0], queries[i][1]+1):
            sum_val += arr[j-1]
        print(sum_val)
test(m)