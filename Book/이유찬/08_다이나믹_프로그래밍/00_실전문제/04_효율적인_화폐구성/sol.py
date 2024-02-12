import sys
sys.stdin = open('input.txt')


def ulmana(N, M, field):
    # 최소 화폐 개수를 저장하는 배열을 초기화
    dp = [float('inf')] * (M + 1) 
    # 0원을 만드는 데는 0개
    dp[0] = 0

    for i in range(1, M + 1):
        for j in range(N):
            if i - field[j] >= 0:
                # 최소 화폐 개수를 계산
                dp[i] = min(dp[i], dp[i - field[j]] + 1)

    return dp[M] if dp[M] != float('inf') else -1  # 만들 수 없는 경우 -1을 반환


T = int(input())
for test_case in range(1, T+1):
    # N과 M 입력받기
    N, M = map(int, input().split())
    # 각 화폐의 가치를 입력받은 배열
    field = [int(input()) for _ in range(N)]

    # 출력
    result = ulmana(N, M, field)
    print(result)  # 결과 출력
