import sys

sys.stdin = open('input.txt')

#           상       우상     우      우하    하       좌하      좌       좌상
delta = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def change_color(board, i, j, color):
    N = len(board)
    # 8 방향 탐색
    for k in range(8):
        ni = i + delta[k][0]
        nj = j + delta[k][1]

        visited = []
        # 오셀로판을 벗어나지 않고, 빈자리가 아니면
        while 0 <= nj < N and 0 <= ni < N and board[ni][nj] != 0:
            visited.append((ni, nj))
            if board[ni][nj] == color:
                break
            ni = ni + delta[k][0]
            nj = nj + delta[k][1]

        if visited:
            li, lj = visited.pop()  # 같은 색 돌을 찾았다면
            if board[li][lj] == color:
                for a, b in visited:  # 찾았으면 사이의 돌을 모두 색 변환
                    board[a][b] = color


T = int(input())

for t in range(1, T + 1):
    # N * N 오셀로판, M 번 게임
    N, M = map(int, input().split())
    # 차례마다 놓는 위치와 색
    turn = [list(map(int, input().split())) for _ in range(M)]
    # 처음 오셀로 판 세팅
    board = [[0] * N for _ in range(N)]
    board[N // 2 - 1][N // 2 - 1] = board[N // 2][N // 2] = 2
    board[N // 2 - 1][N // 2] = board[N // 2][N // 2 - 1] = 1

    for i in range(M):
        board[turn[i][0] - 1][turn[i][1] - 1] = turn[i][2]  # 돌 놓는 위치
        change_color(board, turn[i][0] - 1, turn[i][1] - 1, turn[i][2])

    B = 0  # 1
    W = 0  # 2
    for i in board:
        B += i.count(1)
        W += i.count(2)
    print(f'#{t} {B} {W}')

