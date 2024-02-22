import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    # N: 화폐 종류, M: 합계(얼마로 만들 것인가)
    N, M = map(int, input().split())
    # 화폐의 가치(얼마짜리 화폐가 있는가)
    money_unit = [int(input()) for _ in range(N)]

    # dp 테이블 => 화폐의 가치는 10,000보다 작거나 같은 자연수이기 때문
    d = [10001] * (M+1)
    # 0원인 경우 화폐를 하나도 사용하지 않을 때 만들 수 있음
    d[0] = 0

    # 화폐 종류만큼 반복
    for i in range(N):
        # 각 화폐 가치의 부터 M 까지 반복(화폐가치보다 작은 값은 만들어 낼 수 없기 때문)
        for j in range(money_unit[i], M+1):
            # 현재 dp에 저장된 값 or 현재 화폐의 가치만큼을 뺀 값에 +1 한 값 중에 작은 값
            d[j] = min(d[j], d[j-money_unit[i]] + 1)

    # 화폐를 만들 수 없으면 -1 출력
    if d[M] == 10001:
        print(f'#{test_case} -1')
    # 만들 수 있으면 최소 몇개의 화폐의 개수가 필요한가
    else:
        print(f'#{test_case} {d[M]}')