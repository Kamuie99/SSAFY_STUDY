import sys
sys.stdin = open('input.txt')

def try_sum(idx, total):
    # 최소값을 저장할 result 변수
    global result
    # 마지막 가로줄까지 갔는데
    if idx == N:
        # total이 최소값 보다 작으면 total을 최소값으로 변경
        if total < result:
            result = total
            return
    # 이미 total 값이 result 보다 크면 더이상 진행 x
    if total > result:
        return
    # 세로로 같은 줄에서 두 개이상의 숫자를 고를 수 없으므로
    for i in range(N):
        # 해당 세로줄이 아직 방문하지 않은 새로줄이라면
        if i not in visited:
            # 해당 세로줄은 사용 된 세로줄
            visited.append(i)
            # 다음 가로줄을 보기 위해 idx 1 증가 후 함수 재호출 total 값 전달
            try_sum(idx+1, total + field[idx][i])
            # 백트래킹, 이전 가로줄로 돌아가기
            visited.pop()

T = int(input())
for test_case in range(1, T+1):
    # N * N 배열의 N
    N = int(input())
    # field 배열에 2차원 배열로 저장
    field = []
    for i in range(N):
        field.append(list(map(int, input().split())))
    # 초기 값을 최대값인 10 * N으로 저장
    result = 10 * N
    # 방문을 확인할 배열
    visited = []
    # 함수 실행
    try_sum(0, 0)
    # 결과출력
    print(f'#{test_case} {result}')