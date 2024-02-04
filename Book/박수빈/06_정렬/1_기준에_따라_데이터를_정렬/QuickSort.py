arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
N = 10

def quick_sort(arry, start, end) :
    if start >= end :   # 원소가 0인 경우 종료
        return
    pivot = start   # 피벗은 첫 번째 원소
    left = pivot + 1
    right = end

    while left <= right :
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and arr[left] <= arr[pivot] :
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and arr[right] >= arr[pivot] :
            right -= 1
        if left > right :   # 엇갈렸다면 작은 데이터와 피벗을 교체
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else :              # 엇갈리지 않았다면 작은 데이터와 큰  데이터를 교체
            arr[left], arr[right] = arr[pivot], arr[right]

        # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행행
        quicksort(arr, start, right-1)
        quick_sort(arr, right+1, end)

quick_sort(arr, 0, N-1)