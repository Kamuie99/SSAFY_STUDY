N, M = list(map(int, input().split()))
arr = list(map(int, input().split()))

# 버블 정렬로 정렬
for i in range(N-1, -1, -1) :
    for j in range(0, i) :
        if arr[j] > arr[j+1] :
            arr[j], arr[j+1] = arr[j+1], arr[j]



# 이진 탐색
start = 0
end = N-1

# start가 end보다 작을 동안 반복한다
while start <= end :
    # tteok : 잘라진 떡의 길이
    tteok = 0
    mid = (start + end) // 2
    # 떡의 개수만큼 반복하면서 잘라진 떡의 길이를 구한다
    for i in range(N) :
        # 만약 중간값보다 더 길어서 잘린 부분이 있다면
        if arr[i] - arr[mid] > 0 :
            # tteok에 그 길이만큼 더한다
            tteok += (arr[i] - arr[mid])
    # 잘라진 길이가 손님이 원하는 길이와 같다면 반복문을 멈춘다
    if tteok == M :
        break
    # 잘라진 길이가 손님이 원하는 길이보다 크다면
    # 절단기의 높이는 더 높여도 되기 때문에
    # 오른쪽 영역을 살펴본다
    elif tteok > M :
        start = mid + 1
    # 잘라진 길이가 손님이 원하는 길이보다 적으면
    # 절단기의 높이를 더 낮춰야 하기 때문에
    # 왼쪽 영역을 살펴본다
    elif tteok < M :
        end = mid - 1
print(arr[mid])
