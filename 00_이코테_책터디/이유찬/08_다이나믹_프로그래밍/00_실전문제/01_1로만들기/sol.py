import sys
sys.stdin = open('input.txt')

def yunsan(N):
    # dp 테이블 초기화
    dp = [0] * (N + 1)

    # 2, 3, 5에 대한 초기 DP값 설정
    for i in range(2, min(6, N + 1)):
        dp[i] = 1

    # 6부터 N까지 각 수에 대해 반복
    for i in range(6, N + 1):
        # 현재 수에서 1을 뺀 경우, 2, 3, 5로 나눈 경우의 최소 값을 찾는다.
        dp[i] = min(dp[i - 1], dp[i // 2] if i % 2 == 0 else float('inf'), dp[i // 3] if i % 3 == 0 else float('inf'), dp[i // 5] if i % 5 == 0 else float('inf')) + 1

    return dp[N]

# Example usage:
X = int(input())
print(yunsan(X))
