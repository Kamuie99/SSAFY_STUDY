# 음료수 얼려먹기
# N * M 크기의 얼음틀
# 구멍이 뚫려 있는 부분은 0
# 칸막이 있으면 1

'''
4 5
00110
00011
11111
00000
'''


def ice(graph, v1, v2):
    global N
    global M

    if v1 < 0 or v1 >= N or v2 < 0 or v2 >= M:
        return False

    elif graph[v1][v2] == '0':  # 방문이 없고 빈 통일 때
        graph[v1][v2] = '1'  # 방문했다고 표시
        # 위치 기준 상하좌우(연결된 노드) 방문
        ice(graph, v1 + 1, v2)
        ice(graph, v1 - 1, v2)
        ice(graph, v1, v2 + 1)
        ice(graph, v1, v2 - 1)
        return True

    else:
        return False


N, M = map(int, input().split())
icebox = [[i for i in input()] for _ in range(N)]

# print(icebox)

cnt = 0

# 얼음통 탐색
for i in range(N):
    for j in range(M):
        if ice(icebox, i, j):
            cnt += 1

print(cnt)

# print(icebox)
