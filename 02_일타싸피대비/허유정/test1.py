# 2사분면
import math
            # 흰공    #1사분면  #2사분면    #3사분면    #4사분면
balls = [[130, 65], [200, 33], [200, 100], [60, 100], [60, 33]]

white_ball = balls[0]

target_ball_1 = balls[1]

target_ball_2 = balls[2]

target_ball_3 = balls[3]

target_ball_4 = balls[4]

# 1사분면 각도구하기
temp1 = abs((target_ball_1[0] - white_ball[0]) / white_ball[1])
temp2 = math.atan(temp1)
temp3 = math.degrees(temp2)
result = temp3
print(f'1사분면 {result}')

# # 4사분면 각도구하기
temp1 = abs(target_ball_2[0] - white_ball[0]) / abs(130-white_ball[1])
temp2 = math.atan(temp1)
temp3 = math.degrees(temp2)
result = 180 - temp3
print(f'4사분면 {result}')

# 3사분면 각도 구하기
temp1 = abs(target_ball_3[1] - white_ball[1]) / abs(white_ball[0])
temp2 = math.atan(temp1)
temp3 = math.degrees(temp2)
result = 270 - temp3
print(f'3사분면 {result}')


# 3사분면 선보다 밑에있는 공때리기
temp1 = abs(target_ball_3[0] - white_ball[0]) / abs(130-white_ball[1])
temp2 = math.atan(temp1)
temp3 = math.degrees(temp2)
result = 180 + temp3
print(f'3사분면 {result}')