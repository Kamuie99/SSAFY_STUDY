# import sys
# sys.stdin = open('input.txt')
###########################################
# B = 1, W = 2
###########################################
T = int(input())
for test_case in range(1, T+1):
    # N과 M값 입력 받기
    N, M = map(int, input().split())
    # 돌 놓는 것들 다 배열에 저장
    stones = []
    for i in range(M):
        x, y, c = map(int, input().split())
        stones.append([x, y, c])
    # 2차원 배열 field 만들기
    field = [[0] * (N+2) for i in range(N+2)]
    # 초기 돌들 투입
    field[N//2][N//2] = 2
    field[N//2][N//2+1] = 1
    field[N//2+1][N//2] = 1
    field[N//2+1][N//2+1] = 2
    # 돌을 하나씩 주어진대로 놓아 봅시다
    for s in stones:
        ################### 델타 탐색 ######################
        dy = [0, 0, -1, +1, -1, -1, +1, +1]
        dx = [-1, +1, 0, 0, -1, +1, -1, +1]
        for i in range(8):
            ######################## 초기화 #########################
            x = s[0]    # 1
            y = s[1]    # 2
            c = s[2]    # 1
            field[y][x] = c
            change = []
            ####################  왼쪽 살펴보기 ######################
            while 0 < x <= N and 0 < y <= N:
                # 벽을 만났거나 돌을 안놓은 곳
                if field[y + dy[i]][x + dx[i]] == 0:
                    change = []
                    break
                # 살펴본 돌색깔이 현재의 돌색깔과 다른 경우
                elif field[y + dy[i]][x + dx[i]] != c:
                    change.append([y + dy[i], x + dx[i]])
                    x += dx[i]
                    y += dy[i]
                # 살펴본 돌색깔이 현재의 돌색깔과 같고 바꿔야 될 돌들이 있는 경우
                elif field[y + dy[i]][x + dx[i]] == c and len(change)>=1:
                    for cha in change:
                        field[cha[0]][cha[1]] = c
                    change = []
                # 살펴본 돌색깔이 현재의 돌색깔과 같은데, 바꿔야 될 돌이 없을 때
                else:
                    break
    ############################### 개수 출력하기 ####################################    
    # 흑돌 개수와 백돌 개수 출력하기
    count_b = 0
    count_w = 0
    # 각각의 돌들의 개수를 세서 각 변수에 저장
    for raw in field:
        temp1 = raw.count(1)
        temp2 = raw.count(2)
        count_b += temp1
        count_w += temp2
    # 테케와 함께 출력
    print(f'#{test_case} {count_b} {count_w}')