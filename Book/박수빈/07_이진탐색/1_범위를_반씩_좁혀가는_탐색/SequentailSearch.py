def sequentail_search(n, target, array) :
    # 각 원소를 하나씩 확인하는데
    for i in range(n) :
        # 현재의 원소가 찾고자 하는 원소와 같으면
        if array[i] == target :
            # 현재의 위치를 반환한다
            # 인덱스는 0부터 시작하고, 위치는 1부터 시작하기 떄문에
            # i에 1을 더한다
            return i + 1


print('생성할 원소 개수를 입력한 후 한 칸을 띄고 찾을 문자열을 입력하세요:')
input_data = input().split()
# n : 생성할 원소의 개수
n = int(input_data[0])
# target : 찾을 문자열
target = input_data[1]

print('앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.')
# N개만큼 문자열 입력
array = input().split()

print(sequentail_search(n, target, array))
