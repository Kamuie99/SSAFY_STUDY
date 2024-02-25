import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
input_arr = list(map(int, input().split()))

input_arr.sort()

max_h = input_arr[-1]

cut = max_h

while True:
    temp = 0
    for i in input_arr:
        if i > cut:
            temp += (i - cut)
    if temp >= M:
        break
    else:
        temp = 0
        cut -= 1

print(cut)
