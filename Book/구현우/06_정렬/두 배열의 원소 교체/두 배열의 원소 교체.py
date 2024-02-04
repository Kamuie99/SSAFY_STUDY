import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8')

N, K = map(int, input().split())
# 최대 K번의 바꿔치기를 통해서 배열 A의 모든 원소의 합의 최댓값을 출력한다.
# A에 있는 리스트 작은값을 B에 있는 큰 값과 바꿔줘야 됨.
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# A의 값을 오름차순으로 정렬
for i in range(N-1,0,-1):
    for j in range(0, i):
        if A[j] > A[j+1]:
            A[j] , A[j+1] = A[j+1] , A[j]

print(A)
# 1 2 3 4 5
# B의 값을 내림차순으로 정렬
for i in range(N-1, 0 , -1):
    for j in range(0, i):
        if B[j] < B[j+1]:
            B[j] , B[j+1] = B[j+1] , B[j]    
print(B)
# 6 6 5 5 5
for i in range(K):
    if A[i] < B[i]:
        A[i],B[i] = B[i], A[i]
    else:
        break
# A의 i번쨰 값이 B의 i번쨰 값보다 작으면
# 서로 바꿔줌.
print(sum(A))
