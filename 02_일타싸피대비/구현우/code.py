'''

피타고라스만 잘 알면 pass는 할 수 있다고 하네요

'''


import math

start = (1,1)
end = (2,2)

a = abs(end[0] - start[0])
print(a)
b = abs(end[1] - start[1])
print(b)
# 피타고라스 정의
r = math.sqrt(a**2 + b**2)
print(r)   # 대각선의 길이

tan = math.atan(b / a)
print(math.degrees(tan))  # 아크 탄젠트

cos = math.acos(b / r)
print(math.degrees(cos))  # 아크 코사인

sin = math.asin(a / r)
print(math.degrees((sin))) # 아크 사인