import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
A = [[0]*M for _ in range(N)]
visited = [[False]*M for _ in range(N)]

# 데이터 삽입
for i in range(N):
    numbers = list(input().strip())
    for j in range(M):
        A[i][j] = int(numbers[j])
        
# 미로를 탐색할 때는 현재 좌표를 기준으로 상,하,좌,우 순서로 인접 노드들을 큐에 삽입하며 방문 체크
# 이때 사용할 상,하,좌,우 계산 리스트
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 전형적인 미로 최단거리(가중치 1)라서 BFS(너비우선탐색)로 풀기
def bfs(i,j):
    queue = deque()
    
    # 시작 좌표 큐에 삽입
    queue.append((i,j))
    visited[i][j] = True
    
    while queue:
        now = queue.popleft()    # (i,j) 튜플
        # 상하좌우 좌표 살피기
        for k in range(4):
            x = now[0] + dx[k]
            y = now[1] + dy[k]
            
            # 좌표가 미로 범위 안에 있어야됨
            if x >= 0 and y >= 0 and x < N and y < M:
                # 해당 좌표 값이 1이거나(이동 가능) 아직 미방문이면 이동
                if A[x][y] == 1 and not visited[x][y]:
                    visited[x][y] = True
                    
                    # 이때 방문한 데이터의 값을 depth의 값으로 저장하기 위해 이전 데이터의 값+1로 업데이트
                    A[x][y] = A[now[0]][now[1]] + 1
                    queue.append((x,y))
bfs(0,0)
print(A[N-1][M-1])