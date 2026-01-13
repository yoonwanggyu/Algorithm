import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 종이 상태 배열
M = [list(map(int,input().split())) for _ in range(10)]
# 색종이 개수
s = [0,5,5,5,5,5]
# 최솟값 갱신을 위해 가장 큰 값을 초기값으로 설정
ans = float('inf')

# 1) 현재 좌표에서 5X5 / 4X4 ..인지 판별하는 함수 
def can_attach(x,y,size):
    # size x size 범위가 종이 크기를 넘지 않는가
    if x + size > 10 or y + size > 10:
        return False
    # 모두 1인가
    for i in range(x,x+size):
        for j in range(y,y+size):
            if M[i][j] != 1 :
                return False
    return True
            
# 2) 사이즈 맞는 색종이 찾았으면 붙이고 모두 0으로 표시하는 함수
def fill(x,y,size,value):
    for i in range(x,x+size):
        for j in range(y,y+size):
            M[i][j] = value    # val=0이면 덮기, val=1이면 되돌리기
            
# 3) 백트래킹 실행 (왼쪽 -> 오른쪽으로 이동하면서 사이즈 보고 붙일 수 있는 색종이 사이트 탐색 후 붙이기)
# 이때 최솟값 비교해서 갱신하기
def backtrack(pos,used):
    global ans
    
    # i) 모든 좌표 탐색한 경우
    if pos == 100:
        ans = min(ans, used)
        return
    
    # ii) 현재까지 사용한 색종이 수가 최솟값 이상이면 더 이상 탐색할 필요 없음
    if used >= ans:
        return
    
    # iii) 현재 위치의 값이 1이라면 색종이 붙여야 하니까 5부터 1까지 색종이 크기 순서대로 검증하면서 붙여보기
    x,y = divmod(pos,10)
        # q, r = divmod(a, b)
        # q = a // b   (몫)
        # r = a % b    (나머지)
        # ex) pos = 37 -> row, col = divmod(37, 10)  # (3, 7)  -> 3행 7열
    if M[x][y] == 1:
        for size in range(5,0,-1):
            # 해당 크기 색종이가 남아 있고 해당 위치에 색종이를 붙일 수 있다면
            if s[size] > 0 and can_attach(x,y,size):
                # 색종이 사용 처리하고 해당 위치 0으로 덮기
                s[size] -= 1
                fill(x,y,size,0)
                
                # 다음 위치로 이동하여 재귀 탐색 수행
                backtrack(pos+1,used+1)
                
                # 탐색 후 색종이 수 복원, 종이 상태 원상 복구
                fill(x,y,size,1)
                s[size] += 1
                
    # iv) 현재 위치의 값이 0이면 색종이 붙일 필요 없으니까 넘어가기
    else:
        backtrack(pos+1,used)
        
backtrack(0,0)
print(ans if ans != float('inf') else -1)