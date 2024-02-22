import sys
sys.stdin = open('input.txt')

def backtrack(line, max_line, hap):
    global min_hap
    if line == max_line:
        if min_hap > hap:
            min_hap = hap
    if min_hap < hap:
        return
    else:
        for i in range(N):
            if not include[i]:
                include[i] = 1
                backtrack(line+1, max_line, hap+arr[line][i])
                include[i] = 0

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    include = [0] * N

    min_hap = 10 * N
    backtrack(0, N, 0)

    print(f'#{tc} {min_hap}')