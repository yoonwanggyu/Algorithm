import sys
from collections import deque
input = sys.stdin.readline

N, L = map(int,input().split())
mydeque = deque()  # 빈 덱 만들기
now = list(map(int,input().split()))

for i in range(N):
    # 덱의 마지막 위치에서부터 현재 값(now[i])보다 큰 값을 덱에서 제거
    while mydeque and mydeque[-1][0] > now[i]:
        mydeque.pop()
    # 덱의 마지막에 (현재 숫자값, 현재 인덱스)를 추가
    mydeque.append((now[i], i))
        # 덱의 맨 앞에 있는 숫자의 위치가 지금 창문의 범위(L)보다 너무 멀리 뒤에 있으면 제거
    if mydeque[0][1] <= i - L:
        mydeque.popleft()
        # 덱의 맨 앞에 있는 숫자가 현재 창문에서 가장 작은 숫자!
    print(mydeque[0][0], end=' ')