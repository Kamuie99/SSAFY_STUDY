arr= [1, 4, 6, 2, 9, 3, 0, 5]


# 오름차순
# for j in range(len(arr)-1, 0, -1):
#     for i in range(j):
#         if arr[i] > arr[i+1]:
#             arr[i], arr[i+1] = arr[i+1], arr[i]
#
# print(arr)

# 내림차순
for j in range(len(arr)-1, 0, -1):
    for i in range(j):
        if arr[i] < arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]

print(arr)