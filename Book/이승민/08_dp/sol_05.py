'''
2 15
2
3

3 4
3
5
7
'''
N, M = map(int, input().split())    #  가지의 화폐, M 원
money = [int(input()) for _ in range(N)]    # 잔돈 리스트
# print(money)

change_lst = [1e9] * (M + 1)    # 돈 다 해도 안 되는 큰숫자

for i in range(N):
    if money[i] <= M:   # 잔돈이 돈보다 작아야됌
        change_lst[money[i]] = 1    # 잔돈의 시작은 1개
    for j in range(M+1):
        # 큰 잔돈으로 거슬러 줄 수 있는지 비교확인
        if j - money[i] > 0:
            change_lst[j] = min(change_lst[j - money[i]] + 1, change_lst[j])

# print(change_lst)
if change_lst[M] >= 1e9:    # 실패시 -1
    print(-1)
else:
    print(change_lst[M])    # 성공시 최소 갯수
