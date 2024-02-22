import sys
sys.stdin = open('input.txt')
T = int(input())  # 테스트 케이스

for t in range(1, T + 1):  # 테스트 케이스만큼 반복
    N, M = map(int, input().split())  # N은 세로 M은 가로
    # 풍선 점수표
    balloons = [list(map(int, input().split())) for _ in range(N)]
    # print(balloons)

    scores = [[0] * M for _ in range(N)]  # 0 점 점수판

    for n in range(N):
        for m in range(M):
            scores[n][m] += balloons[n][m]
            for s in range(1, balloons[n][m] + 1):
                if n - s >= 0:
                    scores[n][m] += balloons[n - s][m]
                if n + s < N:
                    scores[n][m] += balloons[n + s][m]
                if m - s >= 0:
                    scores[n][m] += balloons[n][m - s]
                if m + s < M:
                    scores[n][m] += balloons[n][m + s]

    best_score = []

    for n in range(N):
        best_score.append(max(scores[n]))
    print(f'#{t} {max(best_score)}')