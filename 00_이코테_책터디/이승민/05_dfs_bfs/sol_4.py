# 미로 탈출
# N * M
# 1, 1 > N, M 한 번에 한 칸씩
# 괴물 o = 0 , 괴물 x = 1
# 최소 칸의 갯수 ?  시작 칸, 마지막 칸 모두 포함
'''
5 6
101010
111111
000001
111111
111111
'''
from collections import deque

def miro(graph, v1, v2):
    global N
    global M
    cnt = 0
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([(v1, v2)])
    # 현재 노드를 방문 처리
    graph[v1][v2] = '0'
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        nv1, nv2 = queue.popleft()
        print(f'({nv1},{nv2})', end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in range(N-1):
            for j in range(M-1):
                if graph[i][j] == '1' and (graph[i][j+1] == '1' or graph[i+1][j] == '1'):
                    queue.append((i, j))
                    graph[i][j] = '0'
                    cnt += 1
    return cnt

N, M = map(int, input().split())
board = [[i for i in input()] for _ in range(N)]
print(board)
result = miro(board,0, 0)
print(result)