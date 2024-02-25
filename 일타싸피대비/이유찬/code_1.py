# 1사분면
import math
            # 흰공      # 목적구
balls = [[130, 65], [200, 30]]

white_ball = balls[0]

target_ball = balls[1]


temp1 = abs(target_ball[0] - white_ball[0]) / abs(130-white_ball[1])

temp2 = math.atan(temp1)

temp3 = math.degrees(temp2)


result = 180 - temp3

print(result)


