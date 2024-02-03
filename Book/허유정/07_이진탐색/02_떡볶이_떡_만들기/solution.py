import sys
sys.stdin = open('input.txt')

# N: 떡의 개수, M: 요청한 떡 길이
N, M = map(int, input().split())
height = list(map(int, input().split()))

# 절단기 높이
result = 0

# 절단기 설정 값 = 떡 길이 중 가장 긴 값-1 ~ 1
for i in range(max(height)-1, 0, -1):
    # 잘라낸 떡의 길이 합
    hap = 0
    for he in height:
        if he - i > 0:
            hap += (he - i)
    # 손님이 필요한 길이랑 잘린 떡의 길이의 합이 일치하지 않으면? 오류
    # 최소 M만큼의 떡이 손님에게 갈 수 있게 절단기 높이 조절해야 함
    if hap >= M:
        result = i
        break

print(result)


'''
# 이진 탐색
start = 0
end = max(height)

while start <= end:
    # 잘린 떡의 합
    hap = 0
    center = (start + end) // 2

    for he in height:
        if he - center > 0:
            hap += (he - center)
    if hap < M:
        end = center - 1
    else:
        result = center # 정확하게 일치하지 않아도, 최소한 M 만큼 가져갈 수 있도록 해야하니까!
        start = center + 1

print(result)
'''