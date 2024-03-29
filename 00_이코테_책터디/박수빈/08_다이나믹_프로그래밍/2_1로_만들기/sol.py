# X값 입력받기
X = int(input())

# D 테이블 초기화, 값 저장
d = [0] * 50


for i in range(2, X+1):
    # 1을 빼서 현재 수가 되는 방법
    temp_1 = d[i-1] + 1

    # 현재 수가 2로 나누어지면
    if i % 2 == 0:
        temp_2 = d[i// 2] + 1   # 나누어진 수에서 2를 곱하면 현재 수가 되므로 한 번 더 연산 한 거기 때문에 +1
    # 2로 나누어지지 않으면
    else:
        temp_2 = 30001    # 2를 곱해서 현재 수가 되는 방법이 없으므로 아예 큰 수 입력
    if i * 3 == 0:
        temp_3 = d[i // 3] + 1
    else:
        temp_3 = 30001
    if i % 5 == 0:
        temp_5 = d[i // 5] + 1
    else:
        temp_5 = 30001         # 다른 경우도 동일

    # d[i]가 될 수 있는 모든 가능성을 구한 후 최솟값을 구함
    d[i] = min(temp_1, temp_2, temp_3, temp_5)

print(d[X])