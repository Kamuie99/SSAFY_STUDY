# import sys
# sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    # N * N 배열의 N 값과 파리채 크기 M을 입력받는다.
    N, M = map(int, input().split())
    # 배열 안의 값들을 field에 2차원 배열로 저장한다.
    field = [list(map(int, input().split())) for i in range(N)]
    # N * N 배열에서 M 만큼의 크기를 갖는 네모는 N-M+1개만큼 들어간다.
    A = N - M + 1
    # 파리채가 죽인 파리 수를 저장할 배열
    results = []
    # result에 파리채가 죽인 파리수를 저장하여 results 배열에 저장
    for l in range(A):
        for k in range(A):
            result = 0
            for j in range(M):
                for i in range(M):
                    result += field[j+l][i+k]
            results.append(result)
    # results 배열의 최대값이 파리 최대킬, 테케와 함께 출력
    print(f'#{test_case} {max(results)}')