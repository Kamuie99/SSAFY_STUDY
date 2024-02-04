'''
5
8 3 7 9 2
3
5 7 9
'''
'''
부품 N개
찾는 번호 M개
'''
N = int(input())
N_lst = list(map(int, input().split()))
M = int(input())
M_lst = list(map(int, input().split()))


def ct(alist):
    ctlst = [0] * (max(alist) + 1)
    temp = [0] * len(alist)
    for i in range(len((alist))):
        ctlst[alist[i]] += 1

    for j in range(1, len(ctlst)):
        ctlst[j] += ctlst[j - 1]

    for k in range(len(alist)):
        ctlst[alist[k]] -= 1
        temp[ctlst[alist[k]]] = alist[k]

    return temp


def bi(alist, target, start, end):
    mid = (start + end) // 2
    if alist[mid] == target:
        return 'yes '
    if start > end:
        return 'no '
    elif mid > target:
        end = mid - 1
        return bi(alist, target, start, end)
    elif mid < target:
        start = mid + 1
        return bi(alist, target, start, end)


result1 = ct(N_lst)
result2 = ct(M_lst)
# print(result1)
# print(result2)
for i in result2:
    print(bi(result1, i, 0, N - 1), end = '')
