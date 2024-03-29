arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]   # 정렬할 리스트
N = 10    # arr에 있는 값의 개수

# 첫 번째부터 마지막 이전의 값들을 반복하면서 정렬한다
# 가장 마지막 값은 그 전 값을 비교할 때 자동으로 정렬됨
for i in range(N-1) :
    # 가장 작은 값의 인덱스를 저장할 변수 min_idx
    # 제일 처음에는 정렬해야 할 값들 중에서 제일 앞에 있는 값의 인덱스로 설정
    min_idx = i
    # 기준 위치(i)를 기준으로 그 뒤쪽에 있는 모든 값들과 비교함
    for j in range(i+1, N) :
        # 만약 가장 작은 값이라고 설정한 값보다 더 작은 값이 있다면
        if arr[min_idx] > arr[j] :
            # 그 값의 인덱스를 가장 작은 값의 인덱스로 설정
            min_idx = j
    # 기준 위치(i)를 기준으로 그 뒤쪽에 있는 모든 값들과 비교한 뒤
    # 기준 위치에 있는 값과 가장 작은 값의 위치를 바꿈
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

print(arr)