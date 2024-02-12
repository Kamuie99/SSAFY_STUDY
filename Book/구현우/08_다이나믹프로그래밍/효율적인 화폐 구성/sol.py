import sys
sys.stdin = open('input.txt')

N , M = map(int, input().split())

arr = []
# [2, 3]
for i in range(N):
    arr.append(int(input()))
