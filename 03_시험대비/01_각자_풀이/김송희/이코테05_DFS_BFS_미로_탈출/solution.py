import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
maze = [[0] + list(input()) + [0] for _ in range(N)]
maze.insert(0, [0] * (M + 2))
maze.append([0] * (M + 2))
for i in range(1, N + 1):
    maze[i] = list(map(int, maze[i]))

q = [[1, 1]]
cnt = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[1] * (M + 2) for _ in range(N + 2)]
while q:
    i, j = q.pop(0)   # [1, 1]

    if i == N and j == M:      # 도착했다면
        print(visited[i][j])   # 이때까지 온 거리 출력
        break                  # 반복문 종료
    else:                      # 도착하지 않았다면
        for k in range(4):     # 상하좌우 순회
            if (maze[i + dy[k]][j + dx[k]] == 1) and (visited[i + dy[k]][j + dx[k]] == 1):   # 길이고, 방문하지 않았다면
                q.append([i + dy[k], j + dx[k]])                    # 작업 대기 리스트에 추가
                visited[i + dy[k]][j + dx[k]] = visited[i][j] + 1   # 이때까지 온 거리