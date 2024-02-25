# 선입선출

from collections import deque

#큐(Queue) 구현을 위해 deque 라이브러리 사용
queue = deque()


# 삽입 5 - 삽입 2 - 삽입 3 - 삽입 7 - 삭제 - 삽입 1 - 삽입 4 - 삭제
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()     # 스택에서 pop()는 나중에 들어온 거(가장 오른쪽) 삭제
queue.append(1)     # 큐에서 popleft()는 처음에 들어온 거 부터(가장 왼쪽)부터 삭제
queue.append(4)
queue.popleft()

# 큐는 pop() 사용ㅇ
# queue.pop()


print(queue)   # 먼저 들어온 순서대로
queue.reverse()
print(queue)   # 나중에 들어온 순서대로
print(list(queue))   # 리스트로 변환
