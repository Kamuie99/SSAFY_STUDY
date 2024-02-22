########## 성적이 낮은 순서로 학생 출력하기
import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8')


N = int(input())

students = []
# students라는 빈 리스트 만듦.
for _ in range(N):
    name, score = input().split()
    # name 하고 성적을 인풋받음.
    students.append((name, int(score)))
    # 그 후에 students라는 빈 리스트에다가 어펜드 해줌.
print(students)
# 이순신 95 홍길동 77

for i in range(N-1, 0, -1):
    for j in range(0, i):
        if students[j][1] > students[j+1][1]:
            students[j] , students[j+1] = students[j+1] , students[j]
    # 버블정렬을 통해서 오름차순으로 정렬 후
print(students)
# 홍길동 77 이순신 95
for s in students:
    print(s[0], end = ' ')
# 이름만 뽑아 내야 하므로
# s의 9번쨰 인덱스 값만 출력하면 인덱스 값만 뽑아짐
# 홍길동 이순신