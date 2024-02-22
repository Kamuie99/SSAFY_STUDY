import sys
sys.stdin = open('9490_swea_input.txt')

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    flower = [list(map(int, input().split())) for _ in range(N)]

    cnts = []
    for i in range(N):
        for j in range(M):
            K = flower[i][j]
            cnt = 0
            for k in range(-K, K + 1):
                if 0 <= i + k < N:
                    cnt += flower[i + k][j]   # 세로로 순회하며 꽃가루 수 더하기
                if 0 <= j + k < M:
                    cnt += flower[i][j + k]   # 가로로 순회하며 꽃가루 수 더하기
            cnt -= K                          # 중복되는 기준값 한번 빼기
            cnts.append(cnt)

    print(f'#{t} {max(cnts)}')