import sys

sys.stdin = open('input.txt')
di = [-1, 1, 0, 0]  # 상 하
dj = [0, 0, -1, 1]  # 좌 우

T = int(input())

for t in range(1, T+1):
    # N 줄에 풍선 M 개씩 있다
    N, M = map(int, input().split())
    balloons = [list(map(int, input().split())) for _ in range(N)]  # 풍선 꽃가루 개수
    mx_score = 0    # 최대 점수
    for i in range(N):
        for j in range(M):
            score = balloons[i][j]  # 자기 점수 +
            for l in range(1, balloons[i][j] + 1):  # 풍선에 든 꽃가루 개수만큼
                for k in range(4):  # 4방향 탐색
                    ni = i + (di[k] * l)
                    nj = j + (dj[k] * l)
                    if 0 <= ni < N and 0 <= nj < M:
                        score += balloons[ni][nj]
                if score > mx_score:    # 최대 점수 갱신
                    mx_score = score

    print(f'#{t} {mx_score}')
