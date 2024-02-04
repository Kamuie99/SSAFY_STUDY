########## 성적이 낮은 순서로 학생 출력하기
import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8')


N = int(input())

students = []

for _ in range(N):
    name, score = input().split()
    students.append((name, int(score)))



for i in range(N-1, 0, -1):
    for j in range(0, i):
        if students[j][1] > students[j+1][1]:
            students[j] , students[j+1] = students[j+1] , students[j]

for s in students:
    print(s[0], end = ' ')