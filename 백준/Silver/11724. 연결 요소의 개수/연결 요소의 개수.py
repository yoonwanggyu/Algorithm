import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

# 1) DFS 초기 세팅
    # 노드 수, 엣지 수, 인접 리스트, 방문 리스트
n,m = map(int,input().split())
A = [[] for _ in range(n+1)]
visited = [False] * (n+1)

# 2) DFS 재귀함수로 구현
def dfs(node):
    # 현재 노드 방문 처리
    visited[node] = True
    
    # 현재 노드와 연결된 이웃 노드 돌면서 방문 처리하기(재귀로 처리)
    for i in A[node]:
        if not visited[i]:
            dfs(i)
            
# 3) 데이터 받아서 인접 리스트 A에 집어넣기
for _ in range(m):
    start_node, end_node = map(int,input().split())
    # 방향 없어서 = 양방향이라서 둘다 집어넣기
    A[start_node].append(end_node)
    A[end_node].append(start_node)
        
# 4) 노드 수 만큼 dfs 실행
count = 0
for i in range(1,n+1):
    if not visited[i]:    # 연결 노드 중 방문하지 않았던 노드만 탐색
        count += 1
        dfs(i)
    
print(count)