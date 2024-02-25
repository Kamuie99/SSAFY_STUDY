import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    
    # 0으로 이루어진 벽으로 둘러싸인 2차원 배열 field
    field = [[0] * (M+2)]
    for i in range(N):
        temp = [0] + list(map(int, input().split())) + [0]
        field.append(temp)
    field.append([0] * (M+2))
    
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    hubo = 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            temp_list = []
            for dx, dy in dxy:
                temp = field[i + dx][j + dy]
                temp_list.append(temp)
            temp_list.sort()
            count = 0
            for temp in temp_list:
                if temp != 0 and temp < field[i][j]:
                    count += 1
            if count >= 4:
                hubo += 1
                
    
    print(f'#{test_case} {hubo}')