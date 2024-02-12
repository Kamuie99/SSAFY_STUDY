# 5-8. DFS 예제

# DFS 메서드 정의
def DFS(graph, v, visited) :
    # 현재 노드를 방문 처리
    visited[v] = 1
    print(v, end = ' ')
    # 현재 노드와 연결된 노드를 재귀적으로 반문
    for i in graph[v] :
        if visited[i] == 0 :
            DFS(graph, i, visited)

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
        [],
        [2, 3, 8],
        [1, 7],
        [1, 4, 5],
        [3, 5],
        [3, 4],
        [7],
        [2, 6, 8],
        [1, 7],
        ]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1치원 리스트)
visited = [0] * 9

#정의된 DFS 함수 호출
DFS(graph, 1, visited)