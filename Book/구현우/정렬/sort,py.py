# A = [1, 9, 4, 6, 79, 32, 56, 11, 8, 4, 2, 2, 6, 66, 27]

# 버블정렬 내림

def bubble_sort(A_len , A):
    B = A[:]
    for i in range(A_len -1,0, -1):
        for j in range(i):
            if B[j] < B[j+1]:
                B[j] , B[j+1] = B[j+1] , B[j]

    return B

A = [1, 9, 4, 6, 79, 32, 56, 11, 8, 4, 2, 2, 6, 66, 27]
A_len = len(A)
result = bubble_sort(A_len, A)
print(result)
print(A)
