import sys
from collections import deque
input = sys.stdin.readline
myque = deque()
N = int(input())

# 큐 문제 : 선입선출 성질 활용하기
for i in range(1,N+1):
    myque.append(i)
while len(myque) > 1:
    myque.popleft()
    myque.append(myque.popleft())
print(myque[0])