import sys
sys.stdin = open('input.txt')

dx = [0, 0, -1, 1, -1, 1, -1, 1]
dy = [-1, 1, 0, 0, -1, -1, 1, 1]

def change(x, y):
    for i in range(8):
        change_list = []
        for j in range(1, N):
            nx = x + dx[i] * j
            ny = y + dy[i] * j
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] == 0:
                    break
                elif board[nx][ny] == color:
                    while change_list:
                        cx, cy = change_list.pop()
                        board[cx][cy] = color
                    break
                else:
                    change_list.append((nx, ny))


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [[0] * N for _ in range(N)]
    board[N//2][N//2-1] = board[N//2-1][N//2] = 1
    board[N//2-1][N//2-1] = board[N//2][N//2] = 2

    for _ in range(M):
        y, x, color = map(int, input().split())
        board[x-1][y-1] = color
        change(x-1, y-1)

    cnt_b = cnt_w = 0

    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                cnt_b += 1
            elif board[i][j] == 2:
                cnt_w += 1

    print(f'#{tc} {cnt_b} {cnt_w}')