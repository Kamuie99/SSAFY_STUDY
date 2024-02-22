import sys
sys.stdin = open('16268_swea_input.txt')

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    flower = [[0] + list(map(int, input().split())) + [0] for _ in range(N)]
    flower.append([0] * (M + 2))    # 인덱스 에러 방지를 위해 상하좌우로 0 으로 가벽치기
    flower.insert(0, [0] * (M + 2))

    dx = [1, -1, 0, 0]   # 좌우 탐색
    dy = [0, 0, 1, -1]   # 상하 탐색

    cnts = []
    for i in range(1, N + 1):       # 가운데 풍선을 기준으로
        for j in range(1, M + 1):
            cnt = flower[i][j]      # 가운데 풍선의 꽃가루 수를 담고
            for k in range(4):      # 상하좌우 탐색하며 꽃가루 수 더하기
                cnt += flower[i + dy[k]][j + dx[k]]
            cnts.append(cnt)

    print(f'#{t} {max(cnts)}')