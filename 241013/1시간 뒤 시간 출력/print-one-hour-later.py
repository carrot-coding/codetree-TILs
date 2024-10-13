time = input()
time_arr = time.split(":")
hour = int(time_arr[0])
min_ = int(time_arr[1])
hour_chg = hour + 1
print(f"{hour_chg}:{min_}")