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
    # # 필드 확인
    # for raw in field:
    #     print(raw)
    # 초기 돌들 투입
    field[N//2][N//2] = 2
    field[N//2][N//2+1] = 1
    field[N//2+1][N//2] = 1
    field[N//2+1][N//2+1] = 2
    
###################### 돌 하나씩 놓아보자###############################
    for s in stones:
        
        ################### 초기화 #########################
        x = s[0]    # 1
        y = s[1]    # 2
        c = s[2]    # 1
        field[y][x] = c
        change = []
        ####################  왼쪽 살펴보기 ######################
        while x > 0:
            # 벽을 만났거나 돌을 안놓은 곳
            if field[y][x-1] == 0:
                change = []
                break
            # 살펴본 돌색깔이 현재의 돌색깔과 다른 경우
            elif field[y][x-1] != c:
                change.append(x-1)
                x -= 1
            # 살펴본 돌색깔이 현재의 돌색깔과 같고 바꿔야 될 돌들이 있는 경우
            elif field[y][x-1] == c and len(change)>=1:
                for cha in change:
                    field[y][cha] = c
                change = []
            # 살펴본 돌색깔이 현재의 돌색깔과 같은데, 바꿔야 될 돌이 없을 때
            else:
                break
        ################### 초기화 #########################
        x = s[0]    # 1
        y = s[1]    # 2
        c = s[2]    # 1
        field[y][x] = c
        change = []
        ####################  오른쪽 살펴보기 ######################
        while x <= N:
            # 벽을 만났거나 돌을 안놓은 곳
            if field[y][x+1] == 0:
                change = []
                break
            # 살펴본 돌색깔이 현재의 돌색깔과 다른 경우
            elif field[y][x+1] != c:
                change.append(x+1)
                x += 1
            # 살펴본 돌색깔이 현재의 돌색깔과 같고 바꿔야 될 돌들이 있는 경우
            elif field[y][x+1] == c and len(change)>=1:
                for cha in change:
                    field[y][cha] = c
                change = []
            # 살펴본 돌색깔이 현재의 돌색깔과 같은데, 바꿔야 될 돌이 없을 때
            else:
                break
        ################### 초기화 #########################
        x = s[0]    # 1
        y = s[1]    # 2
        c = s[2]    # 1
        field[y][x] = c
        change = []
        ####################  위쪽 살펴보기 ######################
        while y > 0:
            # 벽을 만났거나 돌을 안놓은 곳
            if field[y-1][x] == 0:
                change = []
                break
            # 살펴본 돌색깔이 현재의 돌색깔과 다른 경우
            elif field[y-1][x] != c:
                change.append(y-1)
                y -= 1
            # 살펴본 돌색깔이 현재의 돌색깔과 같고 바꿔야 될 돌들이 있는 경우
            elif field[y-1][x] == c and len(change)>=1:
                for cha in change:
                    field[cha][x] = c
                change = []
            # 살펴본 돌색깔이 현재의 돌색깔과 같은데, 바꿔야 될 돌이 없을 때
            else:
                break
        ################### 초기화 #########################
        x = s[0]    # 1
        y = s[1]    # 2
        c = s[2]    # 1
        field[y][x] = c
        change = []
        ####################  아래쪽 살펴보기 ######################
        while y <= N:
            # 벽을 만났거나 돌을 안놓은 곳
            if field[y+1][x] == 0:
                change = []
                break
            # 살펴본 돌색깔이 현재의 돌색깔과 다른 경우
            elif field[y+1][x] != c:
                change.append(y+1)
                y += 1
            # 살펴본 돌색깔이 현재의 돌색깔과 같고 바꿔야 될 돌들이 있는 경우
            elif field[y+1][x] == c and len(change)>=1:
                for cha in change:
                    field[cha][x] = c
                change = []
            # 살펴본 돌색깔이 현재의 돌색깔과 같은데, 바꿔야 될 돌이 없을 때
            else:
                break
        # # 필드 확인
        # for raw in field:
        #     print(raw)
        # print()
        ################### 초기화 #########################
        x = s[0]    # 1
        y = s[1]    # 2
        c = s[2]    # 1
        field[y][x] = c
        change = []
        ####################  좌상대각 살펴보기 ######################
        while y > 0 and x > 0:
            # 벽을 만났거나 돌을 안놓은 곳
            if field[y-1][x-1] == 0:
                change = []
                break
            # 살펴본 돌색깔이 현재의 돌색깔과 다른 경우
            elif field[y-1][x-1] != c:
                change.append([y-1, x-1])
                x -= 1
                y -= 1
            # 살펴본 돌색깔이 현재의 돌색깔과 같고 바꿔야 될 돌들이 있는 경우
            elif field[y-1][x-1] == c and len(change)>=1:
                for cha in change:
                    field[cha[0]][cha[1]] = c
                change = []
            # 살펴본 돌색깔이 현재의 돌색깔과 같은데, 바꿔야 될 돌이 없을 때
            else:
                break
        ################### 초기화 #########################
        x = s[0]    # 1
        y = s[1]    # 2
        c = s[2]    # 1
        field[y][x] = c
        change = []
        ####################  우상대각 살펴보기 ######################
        while y > 0 and x <= N:
            # 벽을 만났거나 돌을 안놓은 곳
            if field[y-1][x+1] == 0:
                change = []
                break
            # 살펴본 돌색깔이 현재의 돌색깔과 다른 경우
            elif field[y-1][x+1] != c:
                change.append([y-1, x+1])
                x += 1
                y -= 1
            # 살펴본 돌색깔이 현재의 돌색깔과 같고 바꿔야 될 돌들이 있는 경우
            elif field[y-1][x+1] == c and len(change)>=1:
                for cha in change:
                    field[cha[0]][cha[1]] = c
                change = []
            # 살펴본 돌색깔이 현재의 돌색깔과 같은데, 바꿔야 될 돌이 없을 때
            else:
                break
        ################### 초기화 #########################
        x = s[0]    # 1
        y = s[1]    # 2
        c = s[2]    # 1
        field[y][x] = c
        change = []
        ####################  좌하대각 살펴보기 ######################
        while y <= N and x > 0:
            # 벽을 만났거나 돌을 안놓은 곳
            if field[y+1][x-1] == 0:
                change = []
                break
            # 살펴본 돌색깔이 현재의 돌색깔과 다른 경우
            elif field[y+1][x-1] != c:
                change.append([y+1, x-1])
                x -= 1
                y += 1
            # 살펴본 돌색깔이 현재의 돌색깔과 같고 바꿔야 될 돌들이 있는 경우
            elif field[y+1][x-1] == c and len(change)>=1:
                for cha in change:
                    field[cha[0]][cha[1]] = c
                change = []
            # 살펴본 돌색깔이 현재의 돌색깔과 같은데, 바꿔야 될 돌이 없을 때
            else:
                break
        ################### 초기화 #########################
        x = s[0]    # 1
        y = s[1]    # 2
        c = s[2]    # 1
        field[y][x] = c
        change = []
        ####################  우하대각 살펴보기 ######################
        while y <= N and x <= N:
            # 벽을 만났거나 돌을 안놓은 곳
            if field[y+1][x+1] == 0:
                change = []
                break
            # 살펴본 돌색깔이 현재의 돌색깔과 다른 경우
            elif field[y+1][x+1] != c:
                change.append([y+1, x+1])
                x += 1
                y += 1
            # 살펴본 돌색깔이 현재의 돌색깔과 같고 바꿔야 될 돌들이 있는 경우
            elif field[y+1][x+1] == c and len(change)>=1:
                for cha in change:
                    field[cha[0]][cha[1]] = c
                change = []
            # 살펴본 돌색깔이 현재의 돌색깔과 같은데, 바꿔야 될 돌이 없을 때
            else:
                break
############################### 돌 놓기 끝 #######################################            
            
        # # 필드 확인
        # for raw in field:
        #     print(raw)
        # print()
############################### 개수 출력하기 ####################################    
    # 흑돌 개수와 백돌 개수 출력하기
    count_b = 0
    count_w = 0
        
    for raw in field:
        temp1 = raw.count(1)
        temp2 = raw.count(2)
        count_b += temp1
        count_w += temp2
        
    print(f'#{test_case} {count_b} {count_w}')