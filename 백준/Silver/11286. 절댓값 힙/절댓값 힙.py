import sys
from queue import PriorityQueue

print = sys.stdout.write
input = sys.stdin.readline

N = int(input())

# 우선순위 큐에 절댓값 정렬 기준 삽입
myQueue = PriorityQueue()

for i in range(N):
    request = int(input())
    
    # 1) 0이면 절댓값이 가장 작은 수 출력
    if request == 0:
        if myQueue.empty():
            print('0\n')
        else:
            a = myQueue.get()
            print(str(a[1]) + '\n')
            
    # 2) 0이 아니면 배열에 값 추가
    else:
        myQueue.put((abs(request), request))