import sys
sys.stdin = open('input.txt')

N = int(input())
N_list = list(map(int, input().split()))

M = int(input())
M_list = list(map(int, input().split()))

def binary_search(array, find):
    arr = sorted(array)
    target = find
    start = 0
    end = len(arr) -1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid -1
        else:
            start = mid + 1
    return None

def print_shop(result):
    if result == None:
        print('no', end= ' ')
    else:
        print('yes', end= ' ')
        
for m in M_list:
    result = binary_search(N_list, m)
    print_shop(result)
    