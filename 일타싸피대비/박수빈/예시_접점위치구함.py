import math

# blue_ball
blue_ball = (3,2)
# hole
hole = (4,0)
# my_ball
my_ball = (0,3)
# 구멍과 목적구와의 거리 (루트 함수사용)
hole_to_ball_dis = math.sqrt((hole[0]-blue_ball[0])**2+(hole[1]-blue_ball[1])**2)
hole_to_balls_2r_plus = hole_to_ball_dis + 2
# 구멍과 목적구와의 각도 (atan 함수 사용)
hole_to_ball_radian = math.atan(abs(blue_ball[1]-hole[1])/abs(blue_ball[0]-hole[0]))
hole_to_ball_degrees = math.degrees(hole_to_ball_radian)
#  접점의 위치
x = hole_to_balls_2r_plus * math.cos(hole_to_ball_degrees)
y = hole_to_balls_2r_plus * math.sin(hole_to_ball_degrees)

