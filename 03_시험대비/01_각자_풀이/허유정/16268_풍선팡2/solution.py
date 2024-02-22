import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_hap = 0

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(N):
        for j in range(M):
            hap = arr[i][j]
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < N and 0 <= ny < M:
                    hap += arr[nx][ny]
            if max_hap < hap:
                max_hap = hap

    print(f'#{tc} {max_hap}')