import sys
sys.stdin = open('input.txt')

def food_steal(N, field):
    # dp테이블 초기화
    dp = [0] * N
    
    dp[0] = field[0]
    dp[1] = max(field[0], field[1])

    for i in range(2, N):
        # 현재 창고를 털 경우와 이전 창고를 털고 현재 창고를 털 경우 중 더 큰 값을 저장
        dp[i] = max(dp[i-1], dp[i-2] + field[i])

    return dp[N-1]

# 입력 받기
N = int(input())
field = list(map(int, input().split()))

# 최대 훔칠 수 있는 음식 양 계산하고 출력
print(food_steal(N, field))