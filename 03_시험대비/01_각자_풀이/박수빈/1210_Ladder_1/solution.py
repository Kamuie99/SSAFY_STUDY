import sys
sys.stdin = open('input.txt')


def dfs(x, y) :
    dx = [0, 0, -1]
    dy = [1, -1, 0]

    # 기존에 지나가지 않은 곳이라면 지나가야하니까
    # 지나갔다고 표시해라
    if visited[x][y] == 0 :
        visited[x][y] = 1

    # 좌우, 상 순서대로 살펴봐야함
    for j in range(3) :
        temp_x = x + dx[j]
        temp_y = y + dy[j]

        # 범위 안에 있고
        if 0 <= temp_x < 100 and 0 <= temp_y < 100 :
            # 사다리를 타고 올라갈 수 있고 기존에 간 적이 없다면 올라가는데
            if ladder[temp_x][temp_y] != 0 and visited[temp_x][temp_y] == 0 :
                # x값이 0이라면 출발점에 도착한 거니까 그때의 y값을 반환
                if temp_x == 0 :
                    return temp_y
                # x값이 0이 아니라면 사다리를 타고 올라가야 하니까 재귀함수 이용
                else :
                    result = dfs(temp_x, temp_y)
                    # temp_x = 0일 때 temp_y값을 반환한 것 재귀함수을 썼을 때 반환함
                    if result is not False :
                        return result

    #temp_x = 0일 때 temp_y값을 반환하지 못했으면 False 반환
    return False


# 테스트 케이스 입력
for _ in range(1, 11) :
    # 테스트 케이스 번호
    tc = int(input())
    # 사다리 입력
    ladder = [list(map(int, input().split())) for _ in range(100)]

    # 타고 올라간 지점 표시
    visited = [[0 for _ in range(101)] for _ in range(101)]

    # 도착점에서 출발점으로 가기 위해 도착점을 찾음
    for i in range(len(ladder)) :
        if ladder[-1][i] == 2 :
            # 반환한 값을 result 변수에 저장
            result = dfs(99, i)
            # result 출력력
            print(f'#{tc} {result}')




