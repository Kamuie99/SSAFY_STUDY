def bb_sort(alist):
    for a in range(len(alist), 0, -1):
        for b in range(1, a):
            if alist[b] < alist[b - 1]:
                alist[b], alist[b - 1] = alist[b - 1], alist[b]
    return alist


def max_num(alsit):
    maxi = alsit[0]
    for n in alsit:
        if maxi < n:
            maxi = n
    return maxi

def ct_sort(alist):
    m = max_num(alist)
    ct_list = [0] * (m + 1)
    temp = [0] * len(alist)
    for n in range(len(alist)):
        ct_list[alist[n]] += 1

    for i in range(1, len(ct_list)):
        ct_list[i] += ct_list[i - 1]

    for j in range(len(alist)):
        ct_list[alist[j]] -= 1
        temp[ct_list[alist[j]]] = alist[j]
    return temp

def sel_sort(alist):
    for a in range(len(alist)):
        min_num = alist[a]
        min_idx = len(alist) - 1
        for i in range(a, len(alist)):
            if min_num >= alist[i]:
                min_num = alist[i]
                min_idx = i
        alist[a] , alist[min_idx] = alist[min_idx], alist[a]
    return alist

import sys
sys.stdin = open('input.txt')

# T = int(input())
T = 3
# alist = list(map(int, input().split()))

# for t in range(T):
#     alist.append(int(input()))
alist = [15, 27, 12]

result = sel_sort(alist)
print(result[::-1])

