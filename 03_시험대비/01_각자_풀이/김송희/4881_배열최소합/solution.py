import sys
sys.stdin = open('4881_swea_input.txt')

def f(i, cnt):
    global indexs
    global min_sum

    if i == N:
        if min_sum > cnt:
            min_sum = cnt
    elif cnt > min_sum:
        return
    else:
        for j in range(N):
            if visited[j] == 0:
                visited[j] = 1
                f(i+1, cnt + number[i][j])
                visited[j] = 0

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    number = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    min_sum = 100000000
    f(0, 0)

    print(f'#{t} {min_sum}')