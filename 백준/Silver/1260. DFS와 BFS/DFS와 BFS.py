from collections import deque
N,M,start = map(int,input().split())
A = [[] for _ in range(N+1)]

# 그래프 인접 리스트에 삽입
for _ in range(M):
    a,b = map(int,input().split())
    A[a].append(b)
    A[b].append(a)
    
# 노드 번호가 작은 것을 먼저 방문 -> 오름차순 정렬 필요
for i in range(1,N+1):
    A[i].sort()
    
# DFS 구현
visited = [False] * (N+1)
def dfs(start):
    print(start, end = ' ')
    visited[start] = True
    for i in A[start]:
        if not visited[i]:
            dfs(i)
dfs(start)
print()    # 줄바꿈

# BFS 구현
visited = [False] * (N+1)
def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True
    
    while queue:
        now_node = queue.popleft()
        print(now_node, end = ' ')
        for i in A[now_node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
bfs(start)