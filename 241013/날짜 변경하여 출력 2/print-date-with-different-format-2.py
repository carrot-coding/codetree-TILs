date = input()
date_arr = date.split("-")
year = date_arr[2]
month = date_arr[0]
day = date_arr[1]
print(f"{year}.{month}.{day}")