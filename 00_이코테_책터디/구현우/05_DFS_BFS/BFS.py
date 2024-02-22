# 너비 우선 탐색

# 쉽게 말하면 가까운 노드부터 탐색하는 알고리즘

# 큐를 적용해서 하는듯 ?
# 선입선출 방식

from collections import deque


def bfs(graph, start , visited):
    queue = deque([start])

    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

bfs(graph, 1, visited)

# 1 2 3 8 7 4 5 6