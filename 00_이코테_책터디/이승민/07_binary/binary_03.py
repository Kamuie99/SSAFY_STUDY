'''
4 6
19 15 10 17
'''
# 높이 H
# 떡 갯수 N
# 요청 길이 M
# N, M
N, M = map(int, input().split())
D = list(map(int, input().split()))

#
# for i in range(max(D), -1, -1):
#     cm = 0
#     for d in D:
#         if d > i:
#             cm += (d - i)
#     if cm >= M:
#         print(i)
#         break

def bi(alist, target):
    start, end = 0, max(alist)
    result = 0

    while start <= end:
        mid = (start + end) // 2

        ddeok = 0
        for dd in alist:
            if dd > mid:
                ddeok += (dd - mid)

        if ddeok < target:
            end = mid - 1
        else:
            result = mid
            start = mid + 1

    print(result)


bi(D, M)

