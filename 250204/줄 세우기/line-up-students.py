n = int(input())
students = []

class Student:
    def __init__(self, height, weight, num):
        self.height = height
        self.weight = weight
        self.num = num

for i in range(n):
    height, weight = tuple(map(int, input().split()))
    num = i+1
    students.append(Student(height, weight, num))

students.sort(key=lambda x:(-x.height,-x.weight,x.num))
for student in students:
    print(student.height, student.weight, student.num)
# Write your code here!
