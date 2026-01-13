import sys
input = sys.stdin.readline

N,M = map(int,input().split())
visited = [False] * (N+1)
s = []

# 백트래킹(DFS)으로 1~N 중에서 중복 없이 M개를 뽑아 순서 있게 나열(순열) 
def backtrack():
    if len(s) == M:
        print(*s)
        return
    
    # 1부터 N까지 재귀적으로 돌면서 dfs 탐색
    for i in range(1,N+1):
        if not visited[i]:
            visited[i] = True
            s.append(i)
            backtrack()
            
            # 방금 했던 선택(i를 넣은 것)을 취소하고, 다음 경우의 수를 탐색하기 위해 상태를 원래대로 되돌리는 코드
            s.pop()
            visited[i] = False

backtrack()