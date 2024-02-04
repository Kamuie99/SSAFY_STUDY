# # 재귀함수 이용
# def binary_search(array, target, start, end) :
#    # 시작점이 끝점을 넘어가면 찾는 원소가 없는거임
#    if start > end :
#        return None
#    # 실수일 때는 소수값을 버리고
#    # 몫만 구하기 위해서 //
#    mid = (start + end) // 2
#    # 찾은 경우 중간 인덱스 반환
#    if array[mid] == target :
#         return mid
#    # 중간값보다 타겟이 더 작으면
#    # 중간값을 기준으로 왼쪽 영역에서 찾아야 하기 때문에
#    # 끝점은 중간값- 1
#    elif array[mid] > target :
#        return binary_search(array, target, start, mid-1)
#    # 중간값보다 타겟이 더 크면
#    # 중간값을 기준으로 오른쪽 영역에서 찾아야 하기 때문에
#    # 시작점은 중간값 + 1
#    elif array[mid] < target :
#        return binary_search(array, target, mid+1, end)
#
# n, target = list(map(int, input().split()))
# array = list(map(int, input().split()))
#
# # 인덱스이기 때문에 시작점은 0, 끝점은 n-1
# result = binary_search(array, target, 0,n-1)
# if result == None :
#     print('찾을 원소가 존재하지 않습니다.')
# # 위치는 인덱스 + 1이다
# else :
#     print(result+1)
#
# 반복문 이용
def binary_search(array, target, start, end) :
    # start가 end보다 작을 동안
    while start <= end :
        mid = (start + end ) // 2
        if array[mid] == target :
            return mid
        elif array[mid] > target :
            end = mid - 1
        elif array[mid] < target :
            start = mid + 1
    return None

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None :
    print('찾을 원소가 존재하지 않습니다.')
else :
    print(result+1)