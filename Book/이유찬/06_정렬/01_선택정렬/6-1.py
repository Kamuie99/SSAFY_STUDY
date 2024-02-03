# 선택정렬

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def selection_sorted(array):
    arr = array[:]
    arr_len = len(arr)
    for i in range(arr_len):
        min_idx = i
        for j in range(i+1, arr_len):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

result = selection_sorted(array)

print(*result)    # 0 1 2 3 4 5 6 7 8 9