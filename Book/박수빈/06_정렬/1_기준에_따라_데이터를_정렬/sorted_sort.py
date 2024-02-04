# sorted()
# 원본 자료를 직접 바꾸지 못함
# 새로운 변수로 지정
arr_1 = [7, 5, 3, 2, 7, 1, 8]

result = sorted(arr_1)
print(result)

# sort()
# 원본 자료를 직접 바꿈
# 함수를 적용한 다음 원본만 출력
arr_2 = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

arr_2.sort()
print(arr_2)



arr_3 = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data) :
    return data[1]

result = sorted(arr_3, key=setting)
print(result)