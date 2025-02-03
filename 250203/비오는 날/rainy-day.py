n = int(input())
date = []
day = []
weather = []
weather_ = []

# Write your code here!
class Weather:
    def __init__(self,date,day,weather):
        self.date = date
        self.day = day
        self.weather = weather
for _ in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)
    weather_.append(Weather(d, dy, w))

max_idx = []
for i in range(n):
    weather__ = weather_[i]
    if weather__.weather == 'Rain':
        max_idx.append(i)
for _ in max_idx:
    date_i = max_idx[0]
    if date[i] < date[date_i] :
        date_i = i
print(date[date_i], end=' ')
print(day[date_i], end=' ')
print(weather[date_i], end=' ')