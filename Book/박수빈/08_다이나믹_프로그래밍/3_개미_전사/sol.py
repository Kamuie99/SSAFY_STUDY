# 식량 창고의 개수 N을 입력받는다
N = int(input())
# 식량창고에 있는 식량의 개수를 리스트로 입력받는다
K = list(map(int, input().split()))

# D 테이블 초기화
d = [0] * 50

# 왼쪽부터 살펴볼 때 제일 첫 번재는 자기자신의 식량밖에 가지지 못하므로 d[0] = K[0]
d[0] = K[0]

# 두 번째 식량이 제일 처음 식량보다 많다면 두 번쨰 식량을 훔치는 게 이득이므로
if K[1] > K[0] :
    d[1] = K[1]
# 반대라면 첫 번쨰 식량을 훔치는 게 이득이므로
else :
    d[1] = d[0]

# 세 번쨰 식량부터 N개 째 식량까지 살펴본다
for i in range(2, N) :
    # 현재 식량 이전 식량의 총합이 현재 식량 이전이전 식량과 현재 식량의 총합보다 크다면
    # 현재 식량 이전 식량을 훔치는 게 이득
    if d[i-1] > d[i-2] + K[i] :
        d[i] = d[i-1]
    # 반대라면
    # 현재 식량 이전이전식량과 현재 식량의 총합을 훔치는 게 이득
    else :
        d[i] = d[i-2] + K[i]
print(d[i])