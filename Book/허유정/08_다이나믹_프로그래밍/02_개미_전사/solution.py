import sys
sys.stdin = open('input.txt')

N = int(input())
store = list(map(int, input().split()))

d = [0] * 100

d[0] = store[0]
d[1] = max(store[0], store[1])
for i in range(2, N):
    d[i] = max(d[i-1], d[i-2]+store[i])

print(d[N-1])