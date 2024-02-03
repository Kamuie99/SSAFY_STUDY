import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8')

N = int(input())
students = []
for _ in range(N):
    name, score = map(str, input().split())
    score = int(score)
    students.append({'name': name, 'score' : score})

result = sorted(students, key=lambda students: students['score'])

for r in result:
    print(r['name'], end=' ')