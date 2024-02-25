N = int(input())  # 1 <= N <= 100 스위치 개수
lights = list(map(int, input().split()))  # 1 on / 0 off
P = int(input())  # 1 <= P <= 100 학생 수

for i in range(P):
    a, b = map(int, input().split())

    if a == 1:  # 남학생은 자기 번호 배수의 스위치 상태를 바꾼다.
        for j in range(b - 1, len(lights), b):
            lights[j] = abs(lights[j] - 1)

    if a == 2:  # 여학생은 자기 번호 기준 대칭인 스위치 모두 바꾼다
        lights[b-1] = abs(lights[b-1] - 1)   # 자기 자리 스위치 바꿈
        left, right = b-2, b
        while left >= 0 and right < N and lights[left] == lights[right]:
            lights[left] = lights[right] = abs(lights[left] - 1)
            # lights[right] = abs(lights[right] - 1)
            left -= 1
            right += 1

for l in range(len(lights)):
    print(lights[l], end=' ')
    if (l+1) % 20 == 0:
        print()
print()
# print(*lights)
