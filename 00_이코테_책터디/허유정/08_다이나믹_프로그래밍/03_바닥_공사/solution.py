import sys
sys.stdin = open('input.txt')

# 가로의 길이
N = int(input())

# dp테이블
d = [0] * 1001

# 가로의 길이가 1인 경우 1가지 수 : 2*1 덮개
d[1] = 1
# 가로의 길이가 2인 경우 3가지 수 : 2*2 덮개 / 1*2 덮개 2개 / 2*1 덮개 2개
d[2] = 3
for n in range(3, N+1):
    d[n] = (d[n-2] * 2 + d[n-1]) % 796796

print(d[N])