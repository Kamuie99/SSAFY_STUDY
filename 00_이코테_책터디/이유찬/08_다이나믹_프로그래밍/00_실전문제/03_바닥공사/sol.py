import sys
sys.stdin = open('input.txt')

def fill_floor(N):
    if N == 1:
        return 1
    if N == 2:
        return 3

    dp = [0] * (N + 1)
    dp[1] = 1
    dp[2] = 3

    for i in range(3, N + 1):
        # 경우의 수 계산
        dp[i] = dp[i - 1] + 2 * dp[i - 2]

    return dp[N] % 796796

# 입력 받기
N = int(input())

# 결과 출력
print(fill_floor(N))