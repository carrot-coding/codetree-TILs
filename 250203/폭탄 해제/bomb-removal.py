unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

class Bump :
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second
    
bump1 = Bump(unlock_code, wire_color, seconds)

print(f"code : {bump1.code}")
print(f"color : {bump1.color}")
print(f"second : {bump1.second}")