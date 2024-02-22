import sys
sys.stdin = open('input.txt')
def bck_trk(row, temp_sum):
    global mini
    if temp_sum > mini: # 중간에 합이 최소값 넘어가면 멈춤
        return

    if row == N:    # row == N 이면 리스트 끝
        if temp_sum < mini:
            mini = temp_sum
            return

    for col in range(N):
        if not visited[col]:
            visited[col] = 1    # 방문기록

            # 다음 열에서 방문하지 않은 행 숫자 합
            bck_trk(row + 1, temp_sum + lst[row][col])
            visited[col] = 0    # 방문기록 삭제

T = int(input())

for t in range(1, T + 1):
    N = int(input())    # 3≤ N ≤10

    # 10보다 작은 자연수 N * N
    lst = [list(map(int, input().split())) for _ in range(N)]

    mini = 100  # 10 줄에 자연수 10미만만 자연수 합

    visited = [0] * N

    bck_trk(0, 0)

    print(f'#{t} {mini}')
