import sys
sys.stdin = open('input.txt')

# 전자 매장의 부품 수 N
N = int(input())
# N개 부품의 번호
num_list = list(map(int, input().split()))

# 손님이 문의할 부품 개수(종류) M
M = int(input())
# M개 부품의 번호
search_list = list(map(int, input().split()))

for search in search_list:
    if search in num_list:
        print('yes', end=' ')
    else:
        print('no', end=' ')


# 이진 탐색
'''
def BinarySearch(arr, start, end, target):
    while start <= end:
        center = (start + end) // 2
        
        if arr[center] == target:
            return center
        elif arr[center] > target:
            end = center - 1
        else:
            start = center + 1

# 정렬되어 있어야 이진 정렬이 가능!
num_list.sort()

for search in search_list:
    result = BinarySearch(num_list, 0, N-1, search)

    if result:
        print('yes', end=' ')
    else:
        print('no', end=' ')
'''