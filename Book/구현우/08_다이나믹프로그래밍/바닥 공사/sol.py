import sys
sys.stdin = open('input.txt')

### 
# 2 X N 크기의 바닥을 채우는 방법의 수를 796.796으로 나눈 나머지를 출력
# 1 X 2 ,2 X 1, 2 X 2
# 3개의 덮개를 이용해서 채우자

N = int(input())

dp = [0] * 1001

dp[1] = 1
# 2 X 1의 타일을 채우는 경우의 수는 1가지
dp[2] = 3
# 2 X 2의 타일을 채우는 경우의 수는 3가지
# 2 X 2, 1X2를 2개 , 2 X 1를 2개
for i in range(3, N+1):
    dp[i] = (dp[i-1] + 2 * dp[i-2]) % 796796
    # i-1 까지 길이가 덮개로 덮여져있는 경우 나머지 칸을 채우는 경우는 하나의 경우
    # i-2 까지 길이가 덮개로 덮여져있는 경우 나머지 칸을 채우는 경우는 2가지의 경우
    # 점화식

print(dp[N])


