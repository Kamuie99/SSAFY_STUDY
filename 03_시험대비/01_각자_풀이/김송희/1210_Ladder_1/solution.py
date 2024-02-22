import sys
sys.stdin = open('1210_swea_input.txt')

for t in range(10):
    T = int(input())
    ladder = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]

    column = []               # 기둥 index 만 확인
    for i in range(1, 101):   # range(102) 이지만 제일 끝 원소들은 0이므로 제외하고 순회
        if ladder[0][i] == 1:
            column.append(i)

    finish = ladder[99].index(2)   # 도착지점 인덱스
    x = finish

    for i in range(99, -1, -1):
        if ladder[i][x + 1] == 1:
            x = column[column.index(x) + 1]
        elif ladder[i][x - 1] == 1:
            x = column[column.index(x) - 1]

    print(f'#{T} {x - 1}')