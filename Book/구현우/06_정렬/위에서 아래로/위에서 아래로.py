######### 위에서 아래로

import sys
sys.stdin = open('input.txt')

N = int(input())
# 수열에 속해 있는 수의 개수 N
arr = [int(input())for _ in range(N)]
print(arr)
# 15 27 12

# bubble sort
for i in range(N-1, 0, -1):
    for j in range(0, i):
        if arr[j] < arr[j+1]:
            arr[j] , arr[j+1] = arr[j+1], arr[j]

print(*arr)
# * 리스트 안에 들어있는 원소의 값만 출력 하는것 인듯 ?