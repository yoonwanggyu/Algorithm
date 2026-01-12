import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

N,M = map(int,input().split())
A = [[] for _ in range(N+1)]
visited = [False] * (N+1)
arrive = False

def dfs(node_idx,depth):
    global arrive
    # 깊이가 5이면 도착이므로 함수 종료
    if depth == 5:
        arrive = True
        return
    # 현재 노드 방문 처리
    visited[node_idx] = True
    # 현재 노드 옆 노드 방문
    for neighbor_idx in A[node_idx]:
        if not visited[neighbor_idx]:
            # 노드 방문하면서 들어간 깊이만큼 더해주기(재귀)
            dfs(neighbor_idx, depth+1)
    # 한 경로를 탐색하고 돌아오면 다른 경로를 탐색할 때는 다시 방문 가능하도록
    visited[node_idx] = False
    
# 그래프 데이터 삽입
for _ in range(M):
    a,b = map(int,input().split())
    # 양방향으로 삽입
    A[a].append(b)
    A[b].append(a)
    
# 노드마다 bfs 실행
for i in range(N):
    dfs(i,1)
    if arrive:
        break
print(1 if arrive else 0)