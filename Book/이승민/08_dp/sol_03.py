'''
4
1 3 1 5
'''
N = int(input())
food = list(map(int, input().split()))
food_cnt = [0] * N
food_max = 0
food_cnt[0] = food[0]   # 0번째부터
food_cnt[1] = food[1]   # 1번째부터

for i in range(2, N):
    food_cnt[i] = max(food[i] + food_cnt[i-2], food[i] + food_cnt[i-3]) # 원래 먹는 순서와 그 전에 먹었을 때를 비교

    if food_cnt[i] > food_max:  # 최댓값 입력
        food_max = food_cnt[i]

print(food_max)
print(food_cnt)

d = [0] * 100
d[0] = food[0]
d[1] = max(food[0], food[1])
for i in range(2, N):
    d[i] = max(d[i-1], d[i-2] + food[i])

print(d[N-1])
print(d)