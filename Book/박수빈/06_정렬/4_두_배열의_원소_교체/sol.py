N, K = map(int, input().split())

# A : A 원소들을 입력받음
# B : B 원소들을 입력받음
A = list(map(int, input().split()))
B = list(map(int, input().split()))


# max, min, index 함수
# K만큼 반복하면서
for i in range(K) :
    # 만약 B에서 가장 큰 값이 A에서 가장 작은 값보다 크다면
    # 두 값을 바꾼다
    if min(A) < max(B):
        min_idx_A = A.index(min(A))
        max_idx_B = B.index(max(B))

        A[min_idx_A], B[max_idx_B] = B[max_idx_B], A[min_idx_A]

# A리스트의 합을 출력한다
print(sum(A))


#버블 정렬
# 가장 마지막 위치부터 정렬해야 하기 때문에
# 반복문을 거꾸로 한다
for i in range(N-1, -1, -1) :
    # 제일 첫 번째 위치부터 i-1번째 위치까지 반복한다
    for j in range(0, i) :
        # 만약 기준값이 바로 오른쪽에 있는 값보다 크다면
        # 두 값의 위치를 바꾼다
        if A[j] > A[j+1] :
            A[j], A[j+1] = A[j+1], A[j]
        # B도 반복
        if B[j] > B[j+1] :
            B[j], B[j+1] = B[j+1], B[j]

# K만큼 반복하면서
for i in range(K) :
    # 만약 B에서 가장 큰 값이 A에서 가장 작은 값보다 크다면
    # 두 값을 바꾼다
    if min(A) < max(B) :
        A[i], B[N-1-i] = B[N-1-i], A[i]
# A리스트의 합을 출력한다
print(sum(A))


# 선택 정렬
for i in range(N) :
    # 가장 작은 값의 인덱스 변수를 설정한다
    # 제일 처음에는 기준값의 인덱스로 설정
    min_idx = i
    # 기준값 다음 값부터 N-1 인덱스에 있는 값까지 반복한다
    for j in range(i+1, N) :
        if A[min_idx] > A[j] :
            A[min_idx], A[j] = A[j], A[min_idx]

        if B[min_idx] > B[j] :
            B[min_idx], B[j] = B[j], B[min_idx]

# K만큼 반복하면서
for i in range(K) :
    # 만약 B에서 가장 큰 값이 A에서 가장 작은 값보다 크다면
    # 두 값을 바꾼다
    if min(A) < max(B) :
        A[i], B[N-1-i] = B[N-1-i], A[i]
# A리스트의 합을 출력한다
print(sum(A))

# 카운팅 정렬
# A와 B의 값들과 똑같은 값을 인덱스로 해야한다
# 인덱스는 0으로 시작하기 때문에 1을 더한다
temp_A = [0] * (max(A)+1)
temp_B = [0] * (max(B)+1)

# temp_A와 temp_B를 반복하면서 기준값과 같은 인덱스의 값에 1을 더한다
for i in range(N) :
    temp_A[A[i]] += 1
    temp_B[B[i]] += 1

# 새롭게 정렬할 리스트
lst_A = []
lst_B = []
# temp_A에 있는 최대값만큼 반복한다
for i in range(len(temp_A)) :
    for j in range(temp_A[i]) :
        # temp_A[i]에 있는 값만큼 i를 추가한다
        lst_A.append(i)

# temp_B에 있는 최대값만큼 반복한다
for i in range(len(temp_B)):
    for j in range(temp_B[i]):
        # temp_B[i]에 있는 값만큼 i를 추가한다
        lst_B.append(i)

# K만큼 반복하면서
for i in range(K) :
    # 만약 lst_B에서 가장 큰 값이 lst_A에서 가장 작은 값보다 크다면
    # 두 값을 바꾼다
    if min(A) < max(B) :
        lst_A[i], lst_B[N-1-i] = lst_B[N-1-i], lst_A[i]
# lst_A리스트의 합을 출력한다
print(sum(lst_A))