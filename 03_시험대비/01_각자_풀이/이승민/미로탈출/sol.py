'''
5 6
101010
111111
000001
111111
111111
'''
# N * M , 4 <= N, M <= 200
# 0, 0
# 출구 N-1, M-1
# 괴물 0, 통로 1
# 최소 칸 수
from collections import deque

di = [-1, 1, 0, 0]  # 상 하
dj = [0, 0, -1, 1]  # 좌 우


def bfs():
    q = deque([(0, 0)])
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < M and maze[ni][nj] == 1:
                q.append((ni, nj))
                maze[ni][nj] += maze[i][j]


N, M = map(int, input().split())
maze = [[int(i) for i in input()] for _ in range(N)]
bfs()
print(maze[N - 1][M - 1])
