#후입선출

stack = []

#삽입 5 - 삽입 2 - 삽입 3 - 삽입 7 - 삭제 - 삽입 1 - 삽입 4 - 삭제
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

# 리스트는 leftpop() 사용 X
# stack.leftpop()

print(stack)
print(stack[::-1])