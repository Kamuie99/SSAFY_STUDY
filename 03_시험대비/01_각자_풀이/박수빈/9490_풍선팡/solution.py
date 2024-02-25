import sys
sys.stdin = open('input.txt')

# 테스트 케이스의 개수를 입력받음 
T = int(input())

# 테스트 케이스의 개수만큼 반복함
for tc in range(1, T+1) :
    # N : 세로
    # M : 가로
    N, M = map(int, input().split())
    # 풍선을 리스트로 입력받음
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 최댓값을 받을 변수
    max_num = 0

    # 상하좌우의 풍선을 추가로 터뜨릴 수 있으므로 델타 탐색
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]

    # arr에 있는 모든 값들을 기준으로 잡고 확인해야 하니까
    # 반복문
    for i in range(N) :
        for j in range(M) :
            # i, j : 현재 기준인 좌표
            # result : 현재 기준으로 삼은 풍선을 터뜨려서 
            # 받을 꽃가루의 합
            # 기준 풍선도 더해야하니까 초기값은 본인
            result = arr[i][j]

            # 개수니까 1개~arr[i][j]개
            for k in range(1, arr[i][j] + 1):
                # 상하좌우를 살펴봄
                for l in range(4):
                    temp_i = dx[l] * k + i
                    temp_j = dy[l] * k + j

                    # 임시로 잡은 상하좌우의 값이 범위 안에 있으면
                    if 0 <= temp_i < N and 0 <= temp_j < M:
                        # result에 임시값의 꽃가루 합을 더한다
                        result += arr[temp_i][temp_j]
            # 그렇게 더한 값이 최댓값보다 크면
            # 최댓값은 바뀐다
            if max_num < result:
                max_num = result
    # 최댓값 출력
    print(f'#{tc} {max_num}')
