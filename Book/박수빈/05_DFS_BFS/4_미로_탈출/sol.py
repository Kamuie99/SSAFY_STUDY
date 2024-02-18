'''
5 6
101010
111111
000001
111111
111111

3 3
110
010
011
'''
from collections import deque

# 세로N, 가로M 입력받기
N, M = map(int, input().split())

# 방문 기록을 남길 리스트
visited = [[0 for _ in range(M)] for _ in range(N)]

# 미로를 2차원 리스트로 입력받기
arr = [list(map(int, input())) for _ in range(N)]

def BFS(s) :
    queue = deque()
    # 큐에 시작점 입력
    queue.append(s)    (0, 0)

    # 상하좌우 확인
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # 동빈이의 위치 입력
    # 문제에서는 (1, 1)이었으나 인덱스이므로 (0, 0)
    visited[0][0] = 1

    # 큐에 값이 있을 동안
    while queue :
        # 지금 살펴보는 값은 제일 처음 들어온 값
        now = queue.popleft()

        # 상하좌우에 있는 값을 살펴본다
        for i in range(4) :
            temp_x = now[0]+dx[i]
            temp_y = now[1]+dy[i]

            # 범위를 벗어나면 계속
            if temp_x < 0 or temp_x >= N or temp_y < 0 or temp_y >= M :
                continue
            # 범위 안에 있으면
            else :
                # arr[temp_x][temp_y]를 지나간 적 없고 괴물이 있는 곳이 아니면
                # 조건을 != 0으로 한 이유는
                # arr에 몇 번 움직여서 현재 칸에 도착했는지 표시하기 위해 값을 계속 더했기 때문이다
                if visited[temp_x][temp_y] == 0 and arr[temp_x][temp_y] != 0 :
                    # 살펴볼 큐에 값을 넣고
                    queue.append((temp_x, temp_y))
                    # 지나갔기 때문에 visited에 1을 더한다
                    visited[temp_x][temp_y] = 1

                    # 몇 번 움직여서 도착했는지 계산함
                    arr[temp_x][temp_y] = arr[now[0]][now[1]] + 1

    # 출구에 도착하기 위해 움직인 값을 반환함
    # 인덱스이므로 N-1, M-1
    return arr[N-1][M-1]

# 시작점의 인덱스는 0, 0
print(BFS((0, 0)))