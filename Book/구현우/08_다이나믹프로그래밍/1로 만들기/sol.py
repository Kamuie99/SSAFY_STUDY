import sys
sys.stdin = open('input.txt')

X = int(input())

dp = [0] * 30001 # dp[1] = 0 으로 초기값 설정

for i in range(2,X+1):
    # 1은 0로의 값이기 때문에 2부터 X + 1 까지 돌려준다.
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        # 숫자가 2의 배수인 경우
        dp[i] = min(dp[i], dp[i //2] + 1)
    if i % 3 == 0:
        # 숫자가 3의 배수인 경우
        dp[i] = min(dp[i], dp[i //3] + 1)
    if i % 5 == 0:
        # 숫자가 5의 배수인 경우
        dp[i] = min(dp[i], dp[i //5] + 1)

ans = dp[X]
print(ans)