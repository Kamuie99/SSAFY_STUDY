import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    max_hap = 0

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(N):
        for j in range(M):
            hap = board[i][j]
            for k in range(4):
                for l in range(1, board[i][j]+1):
                    nx = i + dx[k] * l
                    ny = j + dy[k] * l
                    if 0 <= nx < N and 0 <= ny < M:
                        hap += board[nx][ny]
            if max_hap < hap:
                max_hap = hap

    print(f'#{tc} {max_hap}')