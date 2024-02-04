# selection_sort

# 버블정렬이랑 무슨차이 인지 ?
# 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고
# 그 다음 작은 데이터를 선택해 앞에서 두 번째 데이터와 바꾸는 과정을 반복

array = [7,5,9,0,3,1,6,2,4,8]

# 오름차순
for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i] , array[min_index] = array[min_index] , array[i]

print(array)

# 내림차순
for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] < array[j]:
            min_index = j
    array[i] , array[min_index] = array[min_index] , array[i]

print(array)