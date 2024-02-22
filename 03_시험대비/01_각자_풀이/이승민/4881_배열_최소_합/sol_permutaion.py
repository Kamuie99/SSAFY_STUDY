import sys

sys.stdin = open('input.txt')

from itertools import permutations

T = int(input())

for t in range(1, T + 1):
    N = int(input())  # N * N 배열 3<= N <=10
    arr = [list(map(int, input().split())) for _ in range(N)]

    mini = 100  # 10보다 작은 자연수가 10*10 이 최대인 2차원 배열에 주어지기 때문에

    row = [i for i in range(N)]

    rowper = list(permutations(row, N))  # 0~N-1까지 순서 조합
    # print(rowper)
    for per in rowper:
        sum_num = 0
        for i in range(N):
            sum_num += arr[i][per[i]]
            if sum_num > mini:
                break
        if sum_num < mini:
            mini = sum_num

    print(f'#{t} {mini}')

