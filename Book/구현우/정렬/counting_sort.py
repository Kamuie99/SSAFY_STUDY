# 항목들의 순서를 결정하기 위해 집합에 각 항목이 몇 개씩 있는지 세는 작업을 하며,
# 선형 시간에 정렬하는 효율적인 알고리즘.

# 집합 내의 가장 큰 정수가 뭔지 알아야 함

# 데이터를 하나 씩 확인하면 데이터의 값과 동일한 인덱스를 1씩 증가시킨다.
# 반복해서 나온 인덱스 값을 출력해야한다.

array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

# max 쓰지말것을 대비해서
# array 배열에서 최댓값 찾기
max_value = array[0]
for num in array:
    if num > max_value:
        max_value = num

print(max_value)

count = [0] * (max_value + 1)
print(count)  # [0 * 10]의 리스트가 출력됨.


# count라는 리스트의 값을 0으로 초기화해준다음, count의 리스트는 모든 범위를 포함해야 되기 때문에
# array의 최대값에서 1을 증가시켜준 만큼 해줌.



for i in range(len(array)):
    count[array[i]] += 1   # 각 array
    # 인덱스의 해당하는 값이 1씩 증가한다.
print(count)
# [2,2,2,1,1,2,1,1,1,2]


# 오름차순

for i in range(len(count)):
    # 인덱스 0부터 9까지 하나 씩 확인하면서
    for j in range(count[i]):
        # count[i]의 수만큼 반복한다.
        print(i, end = ' ')


# 내림차순
        
for i in range(len(count) -1, -1, -1):
    # 인덱스 0부터 9까지 하나 씩 확인하면서
    for j in range(count[i]):
        # count[i]의 수만큼 반복한다.
        print(i, end = ' ')