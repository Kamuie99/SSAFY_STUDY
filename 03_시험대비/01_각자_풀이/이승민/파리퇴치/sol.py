import sys
sys.stdin = open('input.txt')

# 각 영역의 파리수는 30 이하

T = int(input())
for t in range(1, T + 1):
    # N * N 파리판 5 <= N <= 15
    # M * M 파리채로 죽인 파리채 2 <= M <= N
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]
    # catch = [0*(N-M+1) for _ in range(N-M+1)]
    mx_catch = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            catch = 0
            for k in range(M):
                for l in range(M):
                    catch += flies[i + k][j + l]

            if catch > mx_catch:
                mx_catch = catch

    print(f'#{t} {mx_catch}')
