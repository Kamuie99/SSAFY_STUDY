import sys

sys.stdin = open('input.txt')

di = [0, 0, -1]  # 상 위로만 갈 수 있다.
dj = [-1, 1, 0]  # 좌, 우


def dfs(y, x):
    global end

    ladder[y][x] = 0

    for i in range(3):
        ny = y + di[i]
        nx = x + dj[i]
        if 0 <= nx <= 99 and ladder[ny][nx] == 1:
            if ny == 0:
                end = nx
                return
            dfs(ny, nx)
            break


for _ in range(1, 11):
    t = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    start = 0
    end = 0

    for i in range(100):
        if ladder[99][i] == 2:
            start = i
            break

    dfs(99, start)
    print(f'#{t} {end}')
