import sys
sys.stdin = open('input.txt')
def initialize_board(N):
    board = [[0] * N for _ in range(N)]
    mid = N // 2
    board[mid-1][mid-1] = board[mid][mid] = 2
    board[mid-1][mid] = board[mid][mid-1] = 1
    return board

def is_valid_move(board, color, row, col):
    if board[row][col] != 0:
        return False
    opp_color = 2 if color == 1 else 1
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < len(board) and 0 <= c < len(board) and board[r][c] == opp_color:
            r += dr
            c += dc
            while 0 <= r < len(board) and 0 <= c < len(board):
                if board[r][c] == 0:
                    break
                if board[r][c] == color:
                    return True
                r += dr
                c += dc
    return False

def make_move(board, color, row, col):
    board[row][col] = color
    opp_color = 2 if color == 1 else 1
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    for dr, dc in directions:
        r, c = row + dr, col + dc
        to_flip = []
        while 0 <= r < len(board) and 0 <= c < len(board):
            if board[r][c] == 0:
                break
            if board[r][c] == color:
                for flip_row, flip_col in to_flip:
                    board[flip_row][flip_col] = color
                break
            if board[r][c] == opp_color:
                to_flip.append((r, c))
            r += dr
            c += dc

def count_stones(board):
    black_count = sum(row.count(1) for row in board)
    white_count = sum(row.count(2) for row in board)
    return black_count, white_count

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    board = initialize_board(N)

    for _ in range(M):
        row, col, color = map(int, input().split())
        make_move(board, color, row-1, col-1)

    black_count, white_count = count_stones(board)
    print(f"#{t} {black_count} {white_count}")
