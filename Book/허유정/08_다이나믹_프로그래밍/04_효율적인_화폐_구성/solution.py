import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    money_unit = [int(input()) for _ in range(N)]

    d = [10001] * (M+1)
    d[0] = 0
    for i in range(N):
        for j in range(money_unit[i], M+1):
            d[j] = min(d[j], d[j-money_unit[i]] + 1)

    if d[M] == 10001:
        print(f'#{test_case} -1')
    else:
        print(f'#{test_case} {d[M]}')