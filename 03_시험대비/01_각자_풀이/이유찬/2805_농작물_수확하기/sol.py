import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())    # 7
    field = [list(map(int, input())) for i in range(N)]


    center = (N-1)//2   # 3

    # N이 3 이상일때
    
    
    # 뺄꺼 인덱스
    minus_idx = []

    # 좌상 친구들 뺄꺼 인덱스에 넣기
    for i in range(center): # 3
        for j in range(center-i):   # 3, 2, 1
            minus_idx.append([i,j])

    # 우상 친구들 뺄꺼 인덱스에 넣기
    for i in range(center): # 3
        for j in range(N-1, center+i, -1):  # (6, 3, -1), (6, 4, -1) (6, 5, -1)
            minus_idx.append([i, j])

    # 좌하 빼주기
    for i in range(N-1, center, -1): # 6, 3, -1
        for j in range(i-center):
            minus_idx.append([i, j])

    # 우하 빼주기
    for i in range(N-1, center, -1):
        for j in range(N-1, N+center-1-i, -1):
            minus_idx.append([i, j])
    
    minus_sum = 0
    for m in minus_idx:
        x = m[0]
        y = m[1]
        minus_sum += field[x][y]
    
    field_sum = 0
    for raw in field:
        temp = sum(raw)
        field_sum += temp
    
    result = field_sum - minus_sum
    
    print(f'#{test_case} {result}')