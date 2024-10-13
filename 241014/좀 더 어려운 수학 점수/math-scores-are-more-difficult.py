inp = input()
arr = inp.split()
a_math = int(arr[0])
a_eng = int(arr[1])

inp = input()
arr = inp.split()
b_math = int(arr[0])
b_eng = int(arr[1])

if a_math > b_math:
    print("A")
elif a_math < b_math:
    print("B")
elif a_eng > b_eng:
    print("A")
else:
    print("B")