import sys
sys.stdin = open('input.txt')

# n * m 크기
n, m = map(int, input().split())
# 얼음틀(0: 구멍 뚫림, 1: 칸막이)
graph = [list(map(int, input())) for _ in range(n)]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 한 번에 만들 수 있는 아이스크림의 개수
# 0이 있는 한 지점을 기준으로 상하좌우를 검색하면서 연결되어 있는 모든 0을 연결하면 하나의 아이스크림
# 연결된 0을 모두 탐색 했을 때를 판단하여 결과값 +1

def dfs(x, y):
    if graph[x][y] == 0:
        # 해당 지점이 0일 때, 다시 탐색하지 않도록 하기 위해 1로 채워줌
        graph[x][y] = 1
        # 상하좌우 4방향을 탐색하면서 주변에 0이 없을 때까지 반복
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                dfs(nx, ny)
        # 연결된 0을 모두 탐색한 후 True를 전달
        return True
    # 함수에 들어온 값이 0이 아니면 바로 False를 전달하고 종료
    # 다음 위치의 값이 0인지 탐색
    return False

result = 0
for i in range(n):
    for j in range(m):
        # 연결된 0을 모두 탐색한 후의 값이 True이면 결과 +1
        if dfs(i, j) == True:
            result += 1

print(result)