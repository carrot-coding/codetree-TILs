n = int(input())
locations = []

class Location:
    def __init__(self,a,b,num):
        self.a=a
        self.b=b
        self.num=num

for i in range(n):
    a, b = tuple(map(int,input().split()))
    locations.append(Location(a,b,i+1))

# for idx, location in enumerate(locations):
#     location = Location(location.a, location.b, idx+1)
# for location in locations:
#     print(location)

locations2 = sorted(locations, key=lambda x:abs(x.a)+abs(x.b))

# print()
for location in locations2:
    print(location.num)