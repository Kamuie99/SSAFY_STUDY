# import sys
# sys.stdin = open('input.txt')

T = 10
for test_case in range(1, T+1):
    # 테스트 케이스의 번호
    n = int(input())
    # 사다리 값들을 담을 field 배열 초기화 후 저장
    field = []
    for i in range(100):
        temp = list(map(int, input().split()))
        # 제일 왼쪽과 오른쪽에 0으로 이루어진 세로줄을 만들기
        temp_0 = [0] + temp + [0]
        field.append(temp_0)
    # 가로 출발점은 제일 마지막 줄에서 2의 인덱스 값
    garo = field[99].index(2)     # 58
    # 세로 출발점은 제일 마지막 줄
    sero = 99
    # 제일 위에 도착할 때 까지
    while sero > 0:
        # 왼쪽 오른쪽이 둘다 0이면 위로 한칸 올라가기
        if field[sero][garo-1] == 0 and field[sero][garo+1] == 0:
            sero -= 1
        # 만약 왼쪽에 1이 있다면
        if field[sero][garo-1] == 1:
            # 0이 나올때까지 garo 값을 -1
            while field[sero][garo] != 0:
                garo -= 1
            # 마지막까지 갔을때 현재 0의 가로 값을 나타내고 있으므로
            garo += 1   # 가로는 다시 한칸 오른쪽으로
            sero -= 1   # 그 후 위로 한칸 올라가기
        # 만약 오른쪽에 1이 있다면
        if field[sero][garo+1] == 1:
            # 0이 나올때까지 garo 값을 +1
            while field[sero][garo] != 0:
                garo += 1
            # 마지막까지 갔을때 현재 0의 가로 값을 나타내고 있으므로
            garo -= 1   # 가로는 다시 한칸 왼쪽으로
            sero -= 1   # 그 후 위로 한칸 올라가기
    # 왼쪽의 0 세로벽 때문에 -1 해줘야함
    garo -= 1
    # 가로줄 인덱스 값을 테케와 함께 출력
    print(f'#{n} {garo}')