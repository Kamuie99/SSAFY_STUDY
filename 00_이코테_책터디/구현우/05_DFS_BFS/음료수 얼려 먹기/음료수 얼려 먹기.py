import sys
sys.stdin = open('input.txt')


# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())

# n X m 크기의 얼음 틀

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# print(graph)
# graph 리스트에 얼음판의 정보를 저장함.
    
visited = [[False] * m for _ in range(n)]
# 모든 상태를 False로 지정
# 방문한 노드를 표시하기 위해 visited 만들어줌

# 상, 하, 좌, 우로 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

stack = []
result = 0
# 아이스크림 만들어지는 갯수 결과를 result라는 변수에 저장해줄거임.

for i in range(n):
    for j in range(m):
        # 방문하지 않은 노드이고, 얼음이 있는 경우
        if visited[i][j] == False and graph[i][j] == 0:
            stack.append((i, j))
            result += 1
            visited[i][j] = True
            # 방문한곳을 다시 True로 표시

            while stack:
                # 스택이 빌 때까지 반복
                x, y = stack.pop()
                # 스택에서 하나씩 제거해 나감
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    # 현재 위치에서 상하좌우로 이동했을떄 위치를 nx , ny 에 넣어줌

                    if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 0:
                    # 다음 위치가 범위 내에 있으며, 방문하지 않았고,
                    # 또 얼음이 있는 경우에만 한다.  
                        stack.append((nx, ny))
                        # 위치를 또 stack에 추가하고
                        visited[nx][ny] = True
                        # 다시 방문한곳인지 알기 위해서 True로 추가해줌.

print(result)  # 정답 출력


