import sys
sys.stdin = open('input.txt')

# 문제
# 손님이 Mcm를 요청 했을때,
# 절단기에 설정 할 수 있는 높이의 최댓값이 얼마냐 ?
# 입력 받기
N, M = map(int, input().split())
height = list(map(int, input().split()))

# 버블 정렬로 오름차순 정렬
for i in range(N-1):
    for j in range(N-i-1):
        if height[j] > height[j+1]:
            height[j], height[j+1] = height[j+1], height[j]

print(height)
# 10 15 17 19

# 이진 탐색
start = 0
# start의 값을 0
end = height[-1]
# 끝 값을 height의 가장 높은 값
# max 써도 되나 ?
result = 0
# 절단기의 높이

while start <= end:
    # 처음 값이 끝 값보다 낮아질때까지 반복
    total = 0
    # 절단기로 모든 떡을 잘랐을때 남은 떡의 길이 계산
    mid = (start+end) // 2
    # 중간 값 처음 값과 끝 값의 절반
    for i in height:
        if i > mid:
            # 떡의 높이가 더 높을때만 자를 수 있음.
            total += i - mid
    # 남은 떡의 길이가 손님이 요청한 떡의 길이보다 적을 경우,
    # 절단기의 높이를 낮춰야함.
    if total < M:
        end = mid -1
    # 남은 떡의 길이가 손님이 요쳥한 떡의 길이보다 많을 경우,
    # 절단기의 높이를 높여야함.
    else:
        result = mid
        start = mid + 1

print(result)


