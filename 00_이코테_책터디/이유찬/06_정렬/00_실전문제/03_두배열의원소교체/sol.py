import sys
sys.stdin = open('input.txt')

def counting_sorted(array):
    arr = array[:]
    max_arr = max(arr)
    count_arr = [0] * (max_arr + 1)
    
    for a in arr:
        count_arr[a] += 1
    
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]
        
    result_arr = [0] * len(arr)
    
    for a in arr:
        result_arr[count_arr[a]-1] = a
        count_arr[a] -= 1
    
    return result_arr


N, K = map(int, input().split())

A = list(map(int, input().split()))
A_sorted = counting_sorted(A)

B = list(map(int, input().split()))
B_sorted = counting_sorted(B)
B_sorted.reverse()


for i in range(K):
    if A_sorted[i] < B_sorted[i]:
        A_sorted[i], B_sorted[i] = B_sorted[i], A_sorted[i]

print(sum(A_sorted))