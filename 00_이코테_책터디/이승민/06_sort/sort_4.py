'''
5 3
1 2 5 4 3
5 5 6 6 5
'''
'''
N K # N개의 원소, 최대 K번 바꿔치기 (A <> B 원소하나)
# 두 배열 A, B
'''
N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


def bb(alist):  # 버블정렬
    for i in range(len(alist) - 1, 0, -1):
        for j in range(i):
            if alist[j] >= alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]


bb(A)
bb(B)
# print(A)
# print(B)
for k in range(K):  # a 는 앞에서부터 b는 뒤에서 부터
    A[k], B[N - 1 - k] = B[N - 1 - k], A[k]

# print(A)
# print(B)
print(sum(A))
