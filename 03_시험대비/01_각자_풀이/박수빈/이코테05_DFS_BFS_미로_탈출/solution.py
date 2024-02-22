from collections import deque
import sys
sys.stdin = open('input.txt')

dx = [0, 1, 0,  -1]
dy = [1, 0, -1, 0]

def BFS(s) :
    queue = deque()
    queue.append(s)

    while queue :
        t = queue.pop()
        x = t[0]
        y = t[1]

        for i in range(4) :
            temp_x = x + dx[i]
            temp_y = y + dy[i]

            if 0 <= temp_x < N and 0 <= temp_y < M :
                if arr[temp_x][temp_y] == 1 :
                    arr[temp_x][temp_y] = arr[x][y] + 1
                    queue.append((temp_x, temp_y))
    return arr[N-1][M-1]



N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
print(BFS((0, 0)))


