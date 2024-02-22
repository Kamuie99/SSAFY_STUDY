import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    field = [list(map(int, input().split())) for i in range(N)]
    results = []
    for i in range(N):
        for j in range(M):
            temp = 0
            temp += field[i][j]
            # 상
            if i-1 >= 0:
                temp += field[i-1][j]
            # 하
            if i+1 < N:
                temp += field[i+1][j]
            # 좌
            if j-1 >= 0:
                temp += field[i][j-1]
            # 우
            if j+1 < M:
                temp += field[i][j+1]
            results.append(temp)
    print(f'#{test_case} {max(results)}')