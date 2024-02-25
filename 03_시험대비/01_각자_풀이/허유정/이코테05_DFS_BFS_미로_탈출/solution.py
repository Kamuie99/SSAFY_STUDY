import sys
sys.stdin = open('input.txt')
from collections import deque

N, M = map(int, input().split())
miro = [list(map(int, input())) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

x = y = 0
queue = deque()
queue.append((x, y))

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if miro[nx][ny] == 1:
                miro[nx][ny] = miro[x][y] + 1
                queue.append((nx, ny))

print(miro[N-1][M-1])