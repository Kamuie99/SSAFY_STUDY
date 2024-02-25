from collections import deque
import sys
sys.stdin = open('input.txt')

def bfs(field, start_x, start_y):
    n = len(field)
    m = len(field[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # BFS에 사용될 큐, 시작 위치와 거리 1로 초기화
    queue = deque([(start_x, start_y, 1)])
    # 방문한 지점 표시
    visited = [[False] * m for _ in range(n)]
    
    while queue:
        # 큐에서 첫 번째 요소를 pop
        x, y, dist = queue.popleft()
        # 출구 도달 여부 확인
        if x == n - 1 and y == m - 1:  
            return dist
        # 네 방향 모두 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 새로운 위치가 미로 경계 내에 있는지 확인하고 아직 방문하지 않았는지 확인
            if 0 <= nx < n and 0 <= ny < m and field[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True  # 방문 표시
                queue.append((nx, ny, dist + 1))  # 큐에 새 위치를 추가하고 거리를 증가시킴
    
    # 경로를 찾지 못한 경우 -1 반환
    return -1

# N, M을 공백으로 구분하여 입력받기
N, M = map(int, input().split())

# 2차원 리스트에 미로 정보 저장하기
field = []
for i in range(N):
    field.append(list(map(int, input())))

# BFS를 수행한 결과 출력
print(bfs(field, 0, 0))