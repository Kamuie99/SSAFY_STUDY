import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    temp = list(map(int, input().split()))
    
    count = 1
    count_list = []
    for i in range(1, len(temp)):
        if temp[i] > temp[i-1]:
            count += 1
        else:
            count_list.append(count)
            count = 1
        count_list.append(count)
    print(f'#{test_case} {max(count_list)}')