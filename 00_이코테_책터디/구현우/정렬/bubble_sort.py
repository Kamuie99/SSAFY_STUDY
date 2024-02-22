# 오름차순으로 정렬

def bubble_sort(arr_len , arr):
    for i in range(arr_len-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr2 = [10,9,8,7,6,5,4,3,2,1]
arr_len2 = len(arr2)
result = bubble_sort(arr_len2, arr2)
print(result)


# 내림차순으로 정렬

def bubble_sort(arr_len , arr):
    for i in range(arr_len-1, 0, -1):
        for j in range(i):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr2 = [1,2,3,4,5,6,7,8,9,10]
arr_len2 = len(arr2)
result = bubble_sort(arr_len2, arr2)
print(result)


import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8')

N = int(input())
arr = list(map(int, input().split()))

for i in range(N-1):
    for j in range(N-i-1):
        arr[j] > arr[j+1]
        arr[j] , arr[j+1] = arr[j+1] , arr[j]

print(arr)