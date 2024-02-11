import sys
sys.stdin = open('input.txt')

# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 방문한 노드를 표시하기 위한 visited 리스트 생성
visited = [[False] * m for _ in range(n)]

# 상, 하, 좌, 우로 이동하는 함수
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# DFS 함수 정의
stack = []
result = 0

for i in range(n):
    for j in range(m):
        # 방문하지 않은 노드이고, 얼음이 있는 경우
        if not visited[i][j] and graph[i][j] == 0:
            stack.append((i, j))
            result += 1
            visited[i][j] = True

            # 스택을 활용한 DFS
            while stack:
                x, y = stack.pop()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    # 범위를 벗어나지 않고 방문하지 않은 얼음인 경우
                    if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 0:
                        stack.append((nx, ny))
                        visited[nx][ny] = True

print(result)  # 정답 출력


