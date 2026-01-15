from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
A = [[] for _ in range(N+1)]

# 데이터 인접 리스트에 넣기
for _ in range(N):
    numbers = list(map(int,input().split()))
    index = 0
    s = numbers[index]
    index += 1
    while True:
        a = numbers[index]
        if a == -1:
            break
        b = numbers[index+1]
        A[s].append((a,b))
        index += 2
        
# 노드 방문 체크 & 거리 저장
visited = [False] * (N+1)
distance = [0] * (N+1)

# 탐색 결과 경로가 최단 거리로 딱 하나만 나오기 때문에 DFS/BFS 어떤거 써도 무방
# 그런데 문제가 가중치 그래프니까 BFS를 쓴다면 트리 탐색을 큐로 하는 것 + “거리 누적 저장” 이렇게 구현 필요
# bfs
def bfs(start_node):
    queue = deque()
    
    # 시작 노드 넣고 방문 처리
    queue.append(start_node)
    visited[start_node] = True
    
    # 큐가 빌 때까지 반복
    while queue:
        now_node = queue.popleft()
        for i in A[now_node]:
            if not visited[i[0]]:
                visited[i[0]] = True
                queue.append(i[0])
                
                # 거리 누적
                distance[i[0]] = distance[now_node] + i[1]
                
# 트리에서 한 번 탐색으로 찾은 “가장 먼 정점 A”는 지름의 한쪽 끝점이 되고, 그 A에서 다시 한 번 탐색하면 “진짜 최대 거리(지름)”이 나오기 때문에 2번 탐색
# bfs 2번 실행
bfs(1)
far_node = distance.index(max(distance))

    # 초기화
visited = [False] * (N+1)
distance = [0] * (N+1)

bfs(far_node)
print(max(distance))