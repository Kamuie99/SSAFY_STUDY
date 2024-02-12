# 정수 x
# x가 5로 나누어 떨어지면 5로 나눈다.
# x가 5로 나누어 떨어지면 3로 나눈다.
# x가 5로 나누어 떨어지면 2로 나눈다.
# x에서 1을 뺀다.
# 마지막 값 1을 만든다. 연산의 최솟값

X = int(input())
X_lst = [0] * 30001
cnt = 0
def make_one(x):
    global cnt
    if x == 1:
        return cnt

    if (x - 1) % 5 == 0:
        cnt += 1
        return make_one(x-1)

    if x % 5 == 0:
        cnt += 1
        return make_one(x/5)

    elif x % 3 == 0:
        cnt += 1
        return make_one(x/3)

    elif x % 2 == 0:
        cnt += 1
        return make_one(x/2)

    else:
        cnt += 1
        return make_one(x-1)

for i in range(2, X+1):
    # 현재의 수에서 1을 빼는 경우
    X_lst[i] = X_lst[i-1] + 1
    # 2로 나누어 질 때
    if i % 2 == 0:
        X_lst[i] = min(X_lst[i], X_lst[i // 2] + 1)
    # 3으로 나누어 질 때
    if i % 3 == 0:
        X_lst[i] = min(X_lst[i], X_lst[i // 3] + 1)
    # 4로 나누어 질 때
    if i % 5 == 0:
        X_lst[i] = min(X_lst[i], X_lst[i // 5] + 1)



result = make_one(X)
print(result)
print(X_lst[X])
print(X_lst)