import sys
sys.stdin = open('input.txt')

# 좌우상
dx = [0, 0, -1]
dy = [-1, 1, 0]

def search_start():
    for i in range(100):
        if ladder[99][i] == 2:
            return 99, i

def search_end(x, y):
    if x == 0:
        return y

    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 100 and 0 <= ny < 100 and ladder[nx][ny] == 1 and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            return search_end(nx, ny)

for _ in range(1, 11):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    visited = [[0] * 100 for _ in range(100)]

    end_x, end_y = search_start()
    result = search_end(end_x, end_y)

    print(f'#{tc} {result}')