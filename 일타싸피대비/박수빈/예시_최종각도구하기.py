import math

balls = {0: [3, 3], 1: [1, 5]} 

#balls[0][0]: #흰 공의 X좌표
#balls[0][1]: #흰 공의 Y좌표
#balls[1][0]: #1번 공의 X좌표
#balls[1][1]: #1번 공의 y좌표
# 0이 x좌표 , 1이 y좌표

print('1번공 y좌표:', balls[1][1])


# 1. 세기 구하기 power
power_pitago = math.sqrt((balls[0][0]-balls[1][0])**2 + (balls[0][1]-balls[1][1])**2)*40
# power = math.sqrt(power_pitago)*40
print('공 세기',power_pitago)


# 2-1 거리비율 tan = y/x 구하기
x = abs(balls[1][0] - balls[0][0])
y = abs(balls[1][1] - balls[0][1])

biyul = y/x   #거리비율을 구했다!!!!

# 2-2. 각도 구하기
radian = math.atan(biyul)
print('라디안', math.atan(biyul))
gakdo = math.degrees(radian)
print('1사분면 기준 각도', gakdo)

# 2-3. 사분면 생각한 각도 디테일
target_x = balls[1][0] - balls[0][0]
target_y = balls[1][1] - balls[0][1]

if target_x >= 0 and target_y >= 0:
    print('최종 각도',gakdo)
elif target_x >= 0 and target_y < 0:
    print('최종 각도',gakdo+90)
elif target_x < 0 and target_y < 0:
    print('최종 각도',gakdo+180) 
else:
    print('최종 각도',gakdo + 270)   
