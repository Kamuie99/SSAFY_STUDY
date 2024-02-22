import math

start = (0, 0)   # 플레이볼의 좌표
end = (2, 2)    # 쳐야하는 공의 좌표

# 두 공의 거리, 방향(각도)를 알아서 start공을 쳐야한다

# 두 공의 거리를 아는 방법 -> 피타고라스의 정의 이용

a = abs(2 - 0)
b = abs(2 - 0)

# 제곱근을 구해주는 sqrt 함수 이용
# c는 두 공 사이의 거리
c = math.sqrt((a ** 2) + (b ** 2))

# 두 공의 각도를 아는 방법 -> 삼각함수, 라디안 이용

# 아크탄젠트, 아크코사인, 아크사인 이용
tan1 = math.atan(b/a)      # 높이/밑변
degree_tan1 = math.degrees(tan1)

cos1 = math.acos(a/c)     # 밑면/빗변
degree_cos1 = math.degrees(cos1)

sin1 = math.asin(b/c)     # 높이/빗변
degree_sin1 = math.degrees(sin1)


print(c, degree_tan1)
print(c, degree_cos1)
print(c, degree_sin1)