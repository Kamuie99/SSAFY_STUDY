import sys
sys.stdin = open('input.txt')

def f(i, s, N) :
    global min_num
    if i == N :
        if min_num > s :
            min_num = s
    elif min_num <= s :
        return
    else :
        for j in range(i, N) :
            P[i], P[j] = P[j], P[i]
            f(i+1, s+arr[i][P[i]], N)
            P[i], P[j] = P[j], P[i]

T = int(input())

for tc in range(1, T+1) :
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    P = list(range(N))
    min_num = 100

    f(0, 0, N)
    print(f'#{tc} {min_num}')

