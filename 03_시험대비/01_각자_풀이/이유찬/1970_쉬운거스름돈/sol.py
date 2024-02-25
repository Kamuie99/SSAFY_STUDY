import sys
sys.stdin = open('input.txt')

def charge(money):
    field = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    result = [0] * len(field)
    
    for i in range(len(field)):
        if money // int(field[i]):
            result[i] = money // int(field[i])
            money %= int(field[i])
    
    return result
    
T = int(input())
for test_case in range(1, T+1):
    result = charge(int(input()))
    print(f'#{test_case}')
    print(*result)