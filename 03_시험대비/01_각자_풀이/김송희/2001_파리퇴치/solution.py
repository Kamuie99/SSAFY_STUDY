import sys
sys.stdin = open('2001_swea_input.txt')

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]

    cnts = []
    for i in range(N - M + 1):       # 파리채의 좌측상단을 기준으로 삼아 순회
        for j in range(N - M + 1):
            cnt = 0
            for n in range(M):       # 파리채의 크기만큼 순회하며 파리 수 더하기
                for m in range(M):
                    cnt += flies[i + n][j + m]
            cnts.append(cnt)         # 기준점별 파리 수의 합 정보 리스트에 담기

    print(f'#{t} {max(cnts)}')