import sys
from collections import deque
sys.stdin = open('input.txt')

# n * m 크기
n, m = map(int, input().split())
# 미로(0: 괴물이 있는 부분, 1: 없는 부분) => 1을 따라 움직여야 함
graph = [list(map(int, input())) for _ in range(n)]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 움직여야하는 최소칸 => BFS : 시작 지점에서 가장 가까운 노드부터 차례대로 탐색
def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                # 괴물이 있는 부분으면 이동 X
                if graph[nx][ny] == 0:
                    continue
                # 괴물이 없는 부분이면 이동
                # 이동하면서 몇 번째 이동인지 미로에 표시하면서!
                # => 이전 위치 + 1
                elif graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))
    # 몇번째 이동인지 미로에 표시했기 때문에 해당 값에 있는 값을 출력하면 움직인 칸의 수
    return graph[n-1][m-1]

# 현 위치는 (1, 1)이지만, 인덱스는 -1!
print(bfs(0, 0))