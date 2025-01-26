arr = list(map(int, input().split()))
arr_filtered = arr[1::2]
print(sum(arr_filtered), end=' ')
arr_filtered_2 = arr[2::3]
print(f"{sum(arr_filtered_2)/3:.1f}")