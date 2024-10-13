#a의 값이 5인 경우엔 A를
#2의 배수인 경우엔 B를
#둘 다 해당하지 않는 경우에는 아무 값도 출력하지 않습니다.
a = int(input())
if a == 5:
    print("A")
elif a%2 == 0:
    print("B")