# 피보나치 함수를 재귀 함수로 구현
def fibo(n) :
    if n == 1 or n == 2:
        return 1
    else :
        return fibo(n-1) + fibo(n-2)

print(fibo(5))