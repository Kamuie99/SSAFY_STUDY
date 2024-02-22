# import sys
# sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1) :
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]
    # print(arr)

    visited = [[0 for _ in range(N)] for _ in range(N)]
    # 1 : B(흑돌), 2 : W(백돌)
    n = N // 2
    for _ in range(4) :      # 초기 값 설정
        visited[n][n] = 2
        visited[n][n-1] = 1
        visited[n-1][n-1] = 2
        visited[n-1][n] = 1
    # print(visited)

    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]

    for i in range(len(arr)) :
        visited[arr[i][1]-1][arr[i][0]-1] = arr[i][2]       # 위치에 돌을 올려놓음
        for j in range(8) :      # 방향
            for k in range(1, N) :    # 어디까지 갈지
                temp_x = arr[i][1]-1 + (dx[j] * k)
                temp_y = arr[i][0]-1 + (dy[j] * k)
                if 0 <= temp_x < N and 0 <= temp_y < N :
                    if visited[temp_x][temp_y] != arr[i][2] :
                        visited[temp_x][temp_y] = arr[i][2]

    num_b = 0
    num_w = 0
    for s in range(N) :
        for k in range(N) :
            if visited[s][k] == 1 :
                num_b += 1
            elif visited[s][k] == 2 :
                num_w += 1

    print(f'#{tc} {num_b} {num_w}')









