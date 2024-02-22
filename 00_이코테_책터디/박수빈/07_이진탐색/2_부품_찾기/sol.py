N = int(input())
items = list(map(int,input().split()))
M = int(input())
find_items = list(map(int,input().split()))

# 선택 정렬을 이용해 items를 정렬함
# N-1번을 반복하면서
# 가장 작은 값의 인덱스를 기준값의 인덱스인 i라고 설정
for i in range(N-1) :
    min_idx = i
    # items[i+1]부터 items[N-1] 까지의 값으 반복하면서
    # 만약 기준값ㅂ다 작은 값이 있으면 가장 작은 값의 인덱스를 그 값의 인덱스로 함
    for j in range(i+1, N) :
        if items[min_idx] > items[j] :
            min_idx = j
    # 기준값과 가장 작은 값의 위치를 바꿈
    items[i], items[min_idx] = items[min_idx], items[i]


# 순차 탐색
# 찾는 값이 items에 있는지 확인할 변수 설정
check = False
# 찾는 값들을 반복하면서
for item in find_items :
    # items에 있는 값들도 반복한다
    for j in range(N) :
        # 만약 찾는 값이 items에 있다면
        # check는 True가 된다
        if item == items[j] :
            check = True
    # 찾는 값과 items에 있는 값들을 비교한 반복문이 종료된 후
    # check가 True로 바뀌었다면 찾는 값이 있는 것이므로
    # yes 출력
    if check == True :
        print('yes')
    # 바뀌지 않았다면 없다는 것이므로
    # no 출력
    else :
        print('no')

# 이진 탐색
# 찾아야 하는 원소를 반복함
for item in find_items :
    # 시작점은 0이고 끝점은 인덱스가 기준이니 N-1
    start = 0
    end = N - 1
    # 시작점이 끝점보다 작을 동안 반복한다
    while start <= end :
        # 중간값 구함
        mid = (start + end ) // 2
        # 중간값과 item이 같아지면 찾는 원소를 찾았다는 말이니
        # yes를 출력하고 반복문을 종료한다
        if items[mid] == item :
            print('yes')
            break
        # 중간값이 찾는 값보다 크면 찾는 값은 중가값보다 왼쪽 영역에 있다는 말이니
        # end를 중간값에서 1을 뺀 값으로 설정한다
        elif items[mid] > item :
            end = mid - 1
        # 중간값이 찾는 값보다 작으면 찾는 값은 중간값보다 오른쪽 영역에 있다는 말이니
        # start를 중간값에서 1을 더한 값으로 설정한다
        elif items[mid] < item :
            start = mid + 1
    # 원하는 값을 찾아서 반복문이 끝나지 않고 start가 end보다 커서 반복문이 종료됐다면
    # 원하는 원소가 없다는 말이니 no를 출력한다
    if start > end :
        print('no')

