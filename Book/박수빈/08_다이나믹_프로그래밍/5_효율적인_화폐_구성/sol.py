'''
2 15
2
3

3 4
3
5
7
'''
# N가지 종류의 화폐를 이용해 합이 M이 되어야 함
N, M = map(int, input().split())

# 화폐 단위를 입력받음
arr = []
for _ in range(N) :
    arr.append(int(input()))

# D테이블 초기화
# 최소값을 찾아야 하므로 큰 값
d = [10001] * 50
# 0원이 되는 방법은 0
d[0] = 0

# arr에 있는 값이 되는 방법은 그 자신인 값 하나뿐
for num in arr :
    d[num] = 1

for i in range(N) :
    # 가지고 있는 화폐의 단위부터 M원까지의 돈
    for j in range(arr[i], M+1) :
        # 최소한의 화폐 개수이므로 기본값(10001)과 가지고 있는 화폐를 더해서 그 값이 되는 경우를 더함
        d[j] = min(d[j], d[j-arr[i]]+1)

# 더해서 M원이 되는 경우가 없으면 -1 출력
if d[M] == 10001 :
    print(-1)
# 있으면 최소값 출력
else :
    print(d[M])