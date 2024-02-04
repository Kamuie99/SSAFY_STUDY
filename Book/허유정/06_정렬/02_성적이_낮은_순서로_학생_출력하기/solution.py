import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8') # 'cp949' codec can't decode byte 0xed in position 3: illegal multibyte sequence

# 학생의 수
N = int(input())

# N개 만큼의 (학생 이름, 성적)
score_list = [input().split() for _ in range(N)]

# print(score_list)

# 1. 기본 정렬
'''
# 성적이 낮은 순서로 담을 리스트
result = []

result = sorted(score_list, key=lambda x: x[1])

for res in result:
    print(res[0], end=' ')
'''


# 번외 => 이름, 성적을 따로 분리하면 성적 순으로 정렬 가능하지 않을까?
# 물론 이름과 성적 인덱스만 잘 맞춰주면!
names, scores = map(list, zip(*score_list))

# 2. 버블 정렬
'''
for i in range(N-1, 0, -1):
    for j in range(i):
        if scores[j] > scores[j+1]:
            scores[j], scores[j+1] = scores[j+1], scores[j]
            names[j], names[j+1] = names[j+1], names[j]

print(*names)
# print(*scores)
'''

# 3. 선택 정렬
for i in range(len(scores)-1):
    minIdx = i
    for j in range(i+1, len(scores)):
        if scores[minIdx] > scores[j]:
            minIdx = j
    scores[i], scores[minIdx] = scores[minIdx], scores[i]
    names[i], names[minIdx] = names[minIdx], names[i]

print(*names)