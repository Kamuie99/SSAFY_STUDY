import sys
sys.stdin = open('input.txt')

# 목표 : 배열 A의 모든 원소의 합이 최대
# => K번의 연산을 수행하는 동안 배열 A의 가장 작은 값 <-> 배열 B의 가장 큰 값

# N: 배열 크기(길이), K: 연산 횟수
N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for _ in range(K):
    minIdx_A = 0
    maxIdx_B = 0

    for i in range(N):
        if A[minIdx_A] > A[i]:
            minIdx_A = i
        if B[maxIdx_B] < B[i]:
            maxIdx_B = i

    # print(minIdx_A)
    # print(maxIdx_B)

    # A 배열의 가장 작은 값이 B의 가장 큰 값보다 작을 때만 반복!
    # 더 작은 수를 바꾸면 총 합계도 줄어들기 때문
    if A[minIdx_A] < B[maxIdx_B]:
        A[minIdx_A], B[maxIdx_B] = B[maxIdx_B], A[minIdx_A]

print(sum(A))