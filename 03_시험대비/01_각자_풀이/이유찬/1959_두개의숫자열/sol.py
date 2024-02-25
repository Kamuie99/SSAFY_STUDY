import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    result = []
    
    if len(A) < len(B):
        for j in range(M-N+1):
            temp = 0
            for i in range(N):
                temp += A[i] * B[i+j]
            result.append(temp)
    
    if len(A) > len(B):
        for j in range(N-M+1):
            temp = 0
            for i in range(M):
                temp += A[i+j] * B[i]
            result.append(temp)
    
    else:
        temp = 0
        for i in range(N):
            temp += A[i] * B[i]
        result.append(temp)
    
    print(f'#{test_case} {max(result)}')