import sys
sys.stdin = open('input.txt')

# 얼음 틀의 세로길이 N과 가로길이 M 입력 받기.
n, m = map(int, input().split())

# 2차원 리스트 만들기
field = []
for i in range(n):
    field.append(list(map(int, input())))

# DFS를 위한 스택 생성
stack = []

# DFS 구현
result = 0
for i in range(n):
    for j in range(m):
        # 값이 0인 노드 즉 아직 방문하지 않은 노드일 때
        if field[i][j] == 0:
            # 현재 좌표값을 스택에 푸시
            stack.append((i, j))
            result += 1
            # 스택이 빌 때까지 계속, while문이 종료되면 경계 내 전부 방문
            while stack:
                # 스택에서 x, y 를 팝한다.
                x, y = stack.pop()
                # 인전합 셀의 상, 하, 좌, 우 확인
                if x > 0 and field[x-1][y] == 0:
                    stack.append((x-1, y))
                    field[x-1][y] = 1
                if y > 0 and field[x][y-1] == 0:
                    stack.append((x, y-1))
                    field[x][y-1] = 1
                if x < n - 1 and field[x+1][y] == 0:
                    stack.append((x+1, y))
                    field[x+1][y] = 1
                if y < m - 1 and field[x][y+1] == 0:
                    stack.append((x, y+1))
                    field[x][y+1] = 1
# 결과 값 출력
print(result)

