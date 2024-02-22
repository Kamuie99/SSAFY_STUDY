# 반복적으로 구현한 n!
def factorial_iterative(n) :
    result = 1
    # 1부터 n 까지의 수 차레대로 곱하기
    for i in range(1, n +1) :
        result *= i
    return result