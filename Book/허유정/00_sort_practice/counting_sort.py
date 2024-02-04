arr= [1, 4, 6, 2, 9, 3, 0, 5]

# 오름차순
sort_arr = [0] * len(arr)
counts = [0] * (max(arr) + 1)

for num in arr:
    counts[num] += 1

for i in range(1, len(counts)):
    counts[i] += counts[i-1]

for i in range(len(sort_arr)-1, -1, -1):
    counts[arr[i]] -= 1
    sort_arr[counts[arr[i]]] = arr[i]

print(sort_arr)


# 내림차순
sort_arr2 = [0] * len(arr)
counts2 = [0] * (max(arr) + 1)

for num in arr:
    counts2[num] += 1

for i in range(1, len(counts2)):
    counts2[i] += counts2[i-1]

for i in range(len(sort_arr2)-1, -1, -1):
    counts2[arr[i]] -= 1
    sort_arr2[-counts2[arr[i]]-1] = arr[i]

print(sort_arr2)