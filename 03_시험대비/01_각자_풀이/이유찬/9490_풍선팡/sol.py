import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    # N과 M을 입력받아 저장
    N, M = map(int, input().split())
    # field에 2차원 배열 형태로 저장
    field = [list(map(int, input().split())) for i in range(N)]
    # 꽃가루 합을 담을 빈 배열
    results = []
    # 2차원 배열을 순회하면서
    for i in range(N):
        for j in range(M):
            # temp 변수 초기화
            temp = 0
            # 현재 값 할당
            temp = field[i][j]
            # 상하좌우로 얼마만큼 갈지를 t에 저장
            t = temp
            # 해당 풍선의 꽃가루 개수만큼 상하좌우로 이동하여 꽃가루 개수 합
            for k in range(1, t+1):
                # 상
                if 0 <= i-k:
                    temp += field[i-k][j]
                # 하
                if N > i+k:
                    temp += field[i+k][j]
                # 좌
                if 0 <= j-k:
                    temp += field[i][j-k]
                # 우
                if M > j+k:
                    temp += field[i][j+k]
            # 해당 결과값 꽃가루 합 배열에 저장 후 초기화
            results.append(temp)
    # 꽃가루 합들 중 최대 값 출력
    print(f'#{test_case} {max(results)}')
    