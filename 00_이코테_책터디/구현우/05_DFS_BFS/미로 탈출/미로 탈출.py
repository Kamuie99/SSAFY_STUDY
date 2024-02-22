import sys
from collections import deque
sys.stdin = open('input.txt')

# 최소 이동 거리 쓸때 많이 쓴다

# 책에 있는 코드
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()  # []
    # print(queue)
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        # popleft 안쓰고 pop[0] 써줘도 된다.
        # popleft가 무엇 ?
        # 제일 앞의 요소가 삭제된다.
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 찾기 공간을 벗어난 경우와
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if graph[nx][ny] == 0:
                continue
            # 벽을 만난 경우 무시

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n - 1][m - 1]

print(bfs(0,0))