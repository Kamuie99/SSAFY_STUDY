import sys
sys.stdin = open('input.txt')

# 수열에 속해있는 수의 개수
N = int(input())

# 수열 => N개의 수가 한 줄에 한개씩 입력
arr = [int(input()) for _ in range(N)]

# print(arr) # [15, 27, 12]

# 1. 기본 정렬
'''
arr.sort(reverse=True) # 내림차순

print(*arr)
for i in arr:
    print(i, end=' ')
'''

# 2. 버블 정렬
'''
for i in range(N-1, 0, -1):
    for j in range(i):
        # 내림차순이기 때문에 값이 클 때 바꿔줌
        if arr[j] < arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(*arr)
'''

# 3. 카운팅 정렬(1 이상 100,000 이하의 자연수)
'''
counts = [0] * 100001
# 정렬한 결과를 저장할 배열
sort_arr = [0] * N

for i in range(N):
    # 카운트 배열
    counts[arr[i]] += 1

for i in range(1, len(counts)):
    # 누적합 배열
    counts[i] += counts[i-1]

for i in range(N-1, -1, -1):
    counts[arr[i]] -= 1
    sort_arr[counts[arr[i]]] = arr[i]

sort_arr.reverse() # 내림차순으로!
print(*sort_arr)
'''

# 4. 선택 정렬
for i in range(N-1):
    maxIdx = i
    for j in range(1, N):
        # 가장 큰 값이 들어있는 인덱스 찾음
        if arr[j] > arr[maxIdx]:
            maxIdx = j
    # (정렬되지 않은 값들 중) 가장 앞의 갚과 가장 큰 값이 들어있는 인덱스 위치 교환
    arr[i], arr[maxIdx] = arr[maxIdx], arr[i]

print(*arr)