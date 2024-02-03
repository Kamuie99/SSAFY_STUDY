import sys
sys.stdin = open('input.txt')

# 첫째 줄에 수열에 속해 있는 수의 개수 N이 주어진다. (1<=N<=500)
N = int(input())

# 둘째 줄 부터 N+1 번째 줄까지 N개의 수가 입력된다. 수의 범위는 1<=num<=100,000 자연수
arr = []
for _ in range(N):
    arr.append(int(input()))
    
# 버블 정렬
def bubbleSorted(array):
    arr = array[:]
    arr_len = len(array)
    for i in range(arr_len-1):
        for j in range(1, arr_len):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

# 선택 정렬
def selectionSorted(array):
    arr = array[:]
    arr_len = len(array)
    for i in range(arr_len):
        max_idx = i
        for j in range(i+1, arr_len):
            if arr[max_idx] < arr[j]:
                max_idx = j
        arr[max_idx], arr[i] = arr[i], arr[max_idx]
    return arr

# 카운팅 정렬
def countingSorte(array):
    pass

# 주어진 수열이 내림차순으로 졍렬된 결과를 공백으로 구분하여 출력한다.
result = selectionSorted(arr)
print(*result, end=' ')
