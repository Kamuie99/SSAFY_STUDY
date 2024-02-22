import sys
sys.stdin = open('input.txt')

# 테스트 케이스의 개수를 입력받음
T = int(input())

# 테스트 케이스의 개수만큼 반복함
for tc in range(1, T+1) :
    # NxN 배열 안에 파리가 있음
    # MxM 파리채가 있음
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 한 번에 죽일 수 있는 가장 많은 파리의 수를 입력받을 변수
    max_num = 0

    # 모든 값을 기준으로 살펴봐야함
    for i in range(N) :
        for j in range(N) :
            # 한 번에 죽을 수 있는 파리의 값을 입력받을 변수
            result = 0
            # 파리채의 크기만큼 살펴봐야함
            for k in range(M) :
                for l in range(M) :
                    # 기준값이 왼쪽 가장 위에 있을 때
                    # 한 번에 잡을 수 있는 범위
                    temp_i = i + k
                    temp_j = j + l
                    # 범위 내에 있다면
                    if 0 <= temp_i < N and 0 <= temp_j < N :
                        # result에 파리의 개수 더하기
                        result += arr[temp_i][temp_j]
            # 만약 현재 파리 수가 최댓값보다 많으면
            if max_num < result :
                # 최대값은 현재 파리 수
                max_num = result
    # 최댓값 출력
    print(f'#{tc} {max_num}')