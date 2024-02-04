arr= [1, 4, 6, 2, 9, 3, 0, 5]

# 오름차순
# for i in range(len(arr)):
#     minIdx = i
#     for j in range(i+1, len(arr)):
#         if arr[minIdx] > arr[j]:
#             minIdx = j
#     arr[i], arr[minIdx] = arr[minIdx], arr[i]
#
# print(arr)

# 내림차순
for i in range(len(arr)): # k번째로 큰 요소를 찾고싶다 => k까지 반복하여 출력!
    maxIdx = i
    for j in range(i+1, len(arr)):
        if arr[maxIdx] < arr[j]:
            maxIdx = j
    arr[i], arr[maxIdx] = arr[maxIdx], arr[i]

print(arr)