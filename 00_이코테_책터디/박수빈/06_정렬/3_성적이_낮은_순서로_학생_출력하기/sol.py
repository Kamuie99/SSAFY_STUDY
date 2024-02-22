N = int(input())

arr = []
# 반복문으로 이름과 성적을 2차원 리스트로 입력받는다
for _ in range(N) :
    name, score = input().split()
    arr.append([name, int(score)])

# 버블 정렬
# 가장 마지막 위치부터 정렬해야 하기 때문에
# 반복문을 거꾸로 한다
for i in range(N-1, -1, -1) :
    # 제일 첫 번째 위치부터 i-1번째 위치까지 반복한다
    for j in range(0, i) :
        # 만약 기준값이 바로 오른쪽에 있는 값보다 크다면
        # 두 값의 위치를 바꾼다
        if arr[j][1] > arr[j+1][1] :
            arr[j], arr[j+1] = arr[j+1], arr[j]

# arr에 있는 값의 개수만큼 반복하면서
# 이름만 출력한다
for i in range(len(arr)) :
    print(arr[i][0], end = ' ')

# # 선택 정렬
for i in range(N) :
    # 가장 작은 값의 인덱스 변수를 설정한다
    # 제일 처음에는 기준값의 인덱스로 설정
    min_idx= i
    # 기준값 다음 값부터 N-1 인덱스에 있는 값까지 반복한다
    for j in range(i+1, N) :
        # 만약 기준값보다 작은 값이 있다면 가장 작은 값의 인덱스는 그 값이 된다
        if arr[min_idx][1] > arr[j][1] :
            min_idx = j
    # 기준값과 가장 작은 값의 인덱스를 바꾼다
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

# arr에 있는 값의 개수만큼 반복하면서
# 이름만 출력한다
for i in range(len(arr)) :
    print(arr[i][0], end = ' ')


# 카운팅 정렬
# 점수만 입력
temp = []
# 정렬할 리스트
result = []

for i in range(N) :
    temp.append(arr[i][1])

# temp의 값들과 똑같은 값을 인덱스로 해야한다
# 인덱스는 0으로 시작하기 때문에 1을 더한다
cnt = [0] * (max(temp)+1)

# temp를 반복하면서 temp값과 같은 인덱스의 값에 1을 더한다
for j in range(len(temp)) :
    cnt[temp[j]] += 1
# temp에 있는 최대값만큼 반복한다
for i in range(len(cnt)) :
    for j in range(cnt[i]) :
        # cnt[i]에 있는 값만큼 i를 추가한다
        result.append(i)

# result에 있는 값의 개수만큼 반복한다
for i in range(len(result)) :
    # 정렬되지 않은 arr 값도 반복한다
    for j in range(len(arr)) :
        # 순서대로 arr의 이름을 찾아 출력한다
        if result[i] == arr[j][1] :
            print(arr[j][0], end= ' ')

