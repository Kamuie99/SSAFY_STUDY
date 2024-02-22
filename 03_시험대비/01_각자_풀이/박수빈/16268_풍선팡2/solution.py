import sys
sys.stdin = open('input.txt')

# 테스트 케이스의 개수를 입력받음
T = int(input())

# T만큼 반복
for tc in range(1, T+1) :
    # N : x열, M : y열
    N, M = map(int, input().split())
    # 종이 꽃가루의 개수를 입력받음
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 델타탐색
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]

    # 꽃가루 수를 저장할 리스트
    result = []
    # 모든 값들을 기준으로 해서 살펴봄
    for i in range(N) :
        for j in range(M) :
            # 기준으로 한 좌표 + 상하좌우 좌표에 있는 값들을 저장할 리스트
            temp = []
            # 기준인 값을 넣어줌
            temp.append(arr[i][j])
            # 상하좌우 확인
            for k in range(4) :
                temp_i = i + dx[k]
                temp_j = j + dy[k]

                # 임시 값이 범위 안에 있으면
                if 0 <= temp_i< N and 0 <= temp_j < M :
                    # 그 값을 temp리스트에 넣음
                    temp.append(arr[temp_i][temp_j])
                
            # result에 temp에 있는 값들을 합한 값을 넣음
            result.append(sum(temp))
    # result에서 최댓값 출력
    print(f'#{tc} {max(result)}')



