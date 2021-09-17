arr = map(int, '2 3 5 6 7 7'.split())
# print(list(sorted(arr, reverse=True)))
arr = list(sorted(arr, reverse=True))
max_val = max(arr)
while max(arr) == max_val:
    arr.remove(max(arr))
print(arr[0])



