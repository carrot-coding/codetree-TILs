while True:
    n = int(input())
    if n == 25:
        print('Good')
        break
    if n > 25 :
        print('Lower')
        continue
    print('Higher')