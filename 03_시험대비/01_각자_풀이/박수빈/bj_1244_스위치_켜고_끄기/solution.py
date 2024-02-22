import sys
sys.stdin = open('input.txt')


# N : 스위치 개수
N = int(input())
# switch : 스위치의 상태
switch = list(map(int, input().split()))
# students : 학생 수
students = int(input())
# [[성별, 학생이 받은 수], [성별, 학생이 받은 수],...]
arr = [list(map(int, input().split())) for _ in range(students)]

# 인덱스랑 스위치 번호를 같게 하기 위해 제일 처음에 0 추가
switch.insert(0, 0)

# 학생 수만큼 반복
for i in range(len(arr)) :
    # 남학생이라면
    if arr[i][0] == 1 :
        # 자기가 받은 수의 배수인 번호에 있는 스위치의 상태를 바꾼다
        k = arr[i][1]
        r = arr[i][1]
        # 스위치 개수보다 작을 때 동안 반복하면서
        # 스위치 개수를 바꿈
        while r <= N :
            if switch[r] == 0 :
                switch[r] = 1
            else :
                switch[r] = 0
            r += k
    # 여학생이라면
    else :
        # 자기가 받은 번호의 스위치 상태를 바꾼다
        l = arr[i][1]
        if switch[l] == 0 :
            switch[l] = 1
        else :
            switch[l] = 0

        w = 1
        # 범위 안에 있을 동안 
        # 자기가 받은 번호를 중심으로 좌우 대칭인 스위치의
        # 상태를 바꾼다
        while l+w <= N and switch[l-w] == switch[l+w] :
            # 0인덱스는 바꾸면 안되니까
            # 0인덱스에 도달하면 반복문을 멈춘다
            if l-w == 0 :
                break
            # 좌우대칭인 스위치의 상태가 같으면
            # 그 두 스위치의 상태를 바꾼다
            else :
                if switch[l-w] == switch[l+w] == 0 :
                    switch[l-w] = switch[l+w] = 1
                else :
                    switch[l-w] = switch[l+w] = 0
            # 자기가 받은 번호에서 살펴볼 인덱스들은 1씩 멀어진다
            w += 1

# 한 줄에 스무개씩 출력
for i in range(1, len(switch), 20) :
    print(*switch[i:i+20])




