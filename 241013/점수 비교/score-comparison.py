a_score = input()
b_score = input()
a_arr = a_score.split()
b_arr = b_score.split()
a_math = int(a_arr[0])
a_eng = int(a_arr[1])
b_math = int(b_arr[0])
b_eng = int(b_arr[1])
if a_math > b_math and a_eng > b_eng:
    print(1)
else:
    print(0)