import sys
sys.stdin = open('input.txt')

N = int(input())
num_N = list(map(int, input().split()))

M = int(input())
num_M = list(map(int, input().split()))
# 버블정렬을 통해서 먼저 정렬함
for i in range(N-1):
    for j in range(N-i-1):
        if num_N[j] > num_N[j+1]:
            num_N[j], num_N[j+1] = num_N[j+1] , num_N[j]

# print(num_N)
# 2 3 7 8 9

'''
# 순차탐색
for num in num_M:
    if num in num_N:
        print("yes")
    else:
        print("no")
'''


# 이진 탐색
for num in num_M:
    # num이 찾고자 하는 값을 순회할경우
    start = 0
    end = N-1

    while start <= end:
        mid = (start + end) // 2
        # 중간값 지정
        if num_N[mid] == num:
            print('yes')
            break
        # 중간값이 찾고자 하는 값과 같다면
        # yes 출력후 중지
        elif num_N[mid] > num:
            # 중간값이 찾고자 하는 값보다 크다면
            # 왼쪽 영역에 있으므로
            end = mid - 1
            # 끝 값을 중간값에서 1을 뺸 값으로 새로 지정
        elif num_N[mid] < num:
            start = mid + 1
        
    if num_N[mid] != num:
        print('no')

    


        

