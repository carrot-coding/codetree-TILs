n = int(input())
name = []
street_address = []
region = []

for _ in range(n):
    n_i, s_i, r_i = input().split()
    name.append(n_i)
    street_address.append(s_i)
    region.append(r_i)

name2 = sorted(name)
# print(name2[-1])

# Write your code here!
class Student :
    def __init__(self, name, street, region):
        self.name = name
        self.street = street
        self.region = region

for i in range(n) :
    student = Student(name[i],street_address[i],region[i])
    if student.name == name2[-1]:
        print(f"name  {student.name}")
        print(f"addr  {student.street}")
        print(f"city  {student.region}")