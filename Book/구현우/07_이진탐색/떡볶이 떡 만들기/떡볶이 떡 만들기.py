import sys
sys.stdin = open('input.txt')

# 입력 받기
N, M = map(int, input().split())
height = list(map(int, input().split()))

# 버블 정렬로 오름차순 정렬
for i in range(N-1):
    for j in range(N-i-1):
        if height[j] > height[j+1]:
            height[j], height[j+1] = height[j+1], height[j]

print(height)


# 이진 탐색
start = 0
end = height[3]
result = 0

while start <= end:
    total = 0
    mid = (start+end) // 2

    for i in height:
        # 잘랐을떄의 떡 양
        if i > mid:
            total += i - mid
    if total < M:
        end = mid -1

    else:
        result = mid
        start = mid + 1

print(result)


