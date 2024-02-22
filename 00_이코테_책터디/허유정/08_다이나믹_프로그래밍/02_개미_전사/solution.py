import sys
sys.stdin = open('input.txt')

N = int(input())
# 식량 창고
store = list(map(int, input().split()))

# dp테이블
d = [0] * 100

# dp테이블의 첫번째 값은 무조건 식량 창고의 첫번째 값
d[0] = store[0]
# 두번째 값은 첫번째 식량창고를 하나 털거나 그 다음 식량창고를 하나 털거나 둘 중 큰 값
# 인접한 식량창고는 털 수 없기 때문
d[1] = max(store[0], store[1])
# 이후부터는
for i in range(2, N):
    # 이전 식량창고의 값 or 그 전의 식량창고를 털었을 때 + 현재 식량창고의 값 중 큰 값
    d[i] = max(d[i-1], d[i-2]+store[i])

print(d[N-1])