# 피보나치 수열을 통한 다이나믹 프로그래밍

# 피보나치 수열
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)

# print(fibo(4))

# 메모이제이션 이용
d = [0] * 100
# d[1] = 1
# d[2] = 1
def fibo_mem(x):
    if x == 1 or x == 2:
        return 1

    if d[x] != 0:
        return d[x]

    d[x] = fibo_mem(x-1) + fibo_mem(x-2)

    return d[x]

print(fibo_mem(99))
print(d)
