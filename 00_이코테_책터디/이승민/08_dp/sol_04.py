# 가로 N, 세로 2
# 1 * 2, 2 * 1, 2 * 2 로 채우는 경우의 수

N = int(input())
tile = [0] * (N + 1)
tile[1] = 1
tile[2] = 3
tile[3] = 5
for i in range(3, N + 1):
    # 1 * 2 타일이 들어가면 i - 1 의 타일 경우의 수와 같고
    # 2 * 1 이나 2 * 2의 타일이 들어가면 i - 2와 같다
    tile[i] = tile[i - 1] + (2 * tile[i - 2])

print(tile[N] % 796796)