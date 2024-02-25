import sys

sys.stdin = open('input.txt')

for _ in range(1, 11):
    t = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    x = 0

    for i in range(100):
        if ladder[99][i] == 2:
            x = i
            break

    di = [0, 0, -1]  # 상 위로만 갈 수 있다.
    dj = [-1, 1, 0]  # 좌, 우

    i = 99  # 도착지에서 출발

    while i > 0:  # 제일 위에 도착할 때까지
        ladder[i][x] = 0  # 방문 기록
        for j in range(3):
            ni = i + di[j]
            nx = x + dj[j]
            if 0 <= nx <= 99 and ladder[ni][nx] == 1:
                i, x = ni, nx
                break
    else:
        print(f'#{t} {x}')
