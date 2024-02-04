arr = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
cnt = [0] * (max(arr) + 1)


# 정렬할 값들의 개수만큼 반본한다
for i in range(len(arr)) :
    # 정렬할 값들과 같은 번호의 인덱스의 값에 +1을 한다
    # cnt는 0부터 가장 큰 값의 번호를 인덱스로 가짐
    cnt[arr[i]] += 1

# cnt에 있는 값의 개수만큼 반복한다
for i in range(len(cnt)) :
    # cnt[i]의 값은 arr에 있는 i의 개수이다
    # i의 개수만큼 i를 반복적으로 출력한다
    for j in range(cnt[i]) :
        print(i, end= ' ')
