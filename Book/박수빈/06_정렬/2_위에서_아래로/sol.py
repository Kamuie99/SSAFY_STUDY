N = int(input())

arr = []
# N개의 원소가 입력되므로 반복문으로 원소를 입력받고
# 리스트에 추가한다
for _ in range(N) :
    s = int(input())
    arr.append(s)

# 버블 정렬
# 가장 마지막 위치부터 정렬해야 하기 때문에
# 반복문을 거꾸로 한다
for i in range(N-1, -1, -1) :
    # 제일 첫 번째 위치부터 i-1번째 위치까지 반복한다
    for j in range(0, i) :
        # 만약 기준값이 바로 오른쪽에 있는 값보다 크다면
        # 두 값의 위치를 바꾼다
        if arr[j] > arr[j+1] :
            arr[j], arr[j+1] = arr[j+1], arr[j]
    # 반복문을 통해 가장 오른쪽에 있는 위치부터 정렬된다
# 정렬된 오른쪽 칸은 비교할 필요가 없으므로
# 반복할 범위는 점점 줄어든다
print(arr)

# # 선택 정렬
for i in range(N) :
    # 가장 작은 값의 인덱스 변수를 설정한다
    # 제일 처음에는 기준값의 인덱스로 설정
    min_idx = i
    # 기준값 다음 값부터 N-1 인덱스에 있는 값까지 반복한다
    for j in range(i+1, N) :
        # 만약 기준값보다 작은 값이 있다면 가장 작은 값의 인덱스는 그 값이 된다
        if arr[min_idx] > arr[j] :
            min_idx = j
    # 기준값의 인덱스와 가장 작은 값의 인덱스를 서로 바꾼다
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
print(arr)

# 카운팅 정렬
# arr의 값들과 똑같은 값을 인덱스로 해야한다
# 인덱스는 0으로 시작하기 때문에 1을 더한다
cnt = [0] * (max(arr)+1)

# arr를 반복하면서 arr값과 같은 인덱스의 값에 1을 더한다
for i in range(len(arr)) :
    cnt[arr[i]] += 1

result = []
# arr에 있는 최대값만큼 반복한다
for i in range(len(cnt)) :
    # cnt에 있는 값은 0과 arr를 반복할 동안 같은 값의 인덱스의 값에 1을 더한 값이다
    # arr에 같은 값이 여러 개 있으면 그만큼 1을 더한다
    # arr에 없는 값들은 cnt에서 0이기 때문에 j는 0이다
    # 그래서 result.append(i)가 0번 실행됨
    # 반면 cnt[i]에 값이 있으면 그 값만큼 i가 출력됨
    # i == arr에 들어있는 값과 같은 인덱스
    for j in range(cnt[i]) :
        result.append(i)

print(result)
