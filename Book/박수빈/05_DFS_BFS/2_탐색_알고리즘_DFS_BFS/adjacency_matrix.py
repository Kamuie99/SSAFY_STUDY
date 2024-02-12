# # 5-6. 인접 행렬 방식 예제
# INF = 9999999999 #무한 선언
#
# #2차원 리스트를 이용해 인접 행렬 표현
# graph = [
#         [0, 7, 5],
#         [7, 0, INF],
#         [5, INF, 0]
# ]
#
# print(graph)


# 5-7. 인접 리스트 방식 예제
graph = [[] for _ in range(3)]

# 노드0에 연결된 노드 정보 저장(노드, 거리)
graph[0].append((1, 7))
graph[0].append((2, 5))

# 노드1에 연결된 노드 정보 저장(노드, 거리)
graph[1].append((0, 7))

# 노드2에 연결된 노드 정보 저장(노드, 거리)
graph[2].append((0, 5))

print(graph)