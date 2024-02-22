import sys

sys.stdin = open('input.txt')
from collections import deque

di = [0, 0, -1]  # 상 위로만 갈 수 있다.
dj = [-1, 1, 0]  # 좌, 우


def bfs(v1, v2):
    q = deque([(v1, v2)])
    while q:
        y, x = q.popleft()
        if y == 0:
            return x
        ladder[y][x] = 0
        for i in range(3):
            ny = y + di[i]
            nx = x + dj[i]
            if 0 <= nx <= 99 and ladder[ny][nx] == 1:
                q.append((ny, nx))
                break


for _ in range(1, 11):
    t = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    start = 0

    for i in range(100):
        if ladder[99][i] == 2:
            start = i
            break

    end = bfs(99, start)
    print(f'#{t} {end}')
