import sys
input = sys.stdin.readline

N = int(input())

# (row+col) = 오른쪽 위 방향
#      c0 c1 c2 c3
#r0     0  1  2  3
#r1     1  2  3  4
#r2     2  3  4  5
#r3     3  4  5  6
# → diag1[3]이 True면, 이 값이 3인 모든 칸( / 대각선 전체 )에 퀸을 못 놓음

#(row - col + 3(N-1)) = 왼쪽 아래 방향
#      c0 c1 c2 c3
#r0     3  2  1  0
#r1     4  3  2  1
#r2     5  4  3  2
#r3     6  5  4  3
# → diag2[4]가 True면, 이 값이 4인 모든 칸( \ 대각선 전체 )에 퀸을 못 놓음

# 퀸 이동 방향 저장 리스트 (열, / 대각선(오른쪽 위 방향), \ 대각선(왼쪽 아래 방향))
cols = [False] * N                # 열 충돌 여부 저장 리스트
diag1 = [False] * (2 * N - 1)     # / 대각선(row + col) 충돌 여부
diag2 = [False] * (2 * N - 1)     # \ 대각선(row - col + N - 1) 충돌 여부

# 동작 원리
# cols[1] = True  → 1열 사용 중
# diag1[0+1] = diag1[1] = True → / 대각선(인덱스 1) 사용 중
# diag2[0-1+3] = diag2[2] = True → \ 대각선(인덱스 2) 사용 중

# 경우의 수 저장
cnt = 0

# 백트래킹
def backtrack(row):
    global cnt
    # 마지막 행까지 돌면 종료
    if row == N:
        cnt += 1
        return
    
    # 한 행씩 돌면서 퀸 공격 방향(같은 열, 두 가지 경우의 대각석) 피하면서 놓을 수 있는 경우의 수 찾기
    for col in range(N):
        # 현재 행에 있는 퀸 위치에서 같은 열, 양쪽 대각선에는 다른 퀸을 배치하면 안되니까 방문처리
        if not cols[col] and not diag1[row + col] and not diag2[row - col + N - 1]:
            cols[col] = diag1[row + col] = diag2[row - col + N - 1] = True
            backtrack(row+1)
           
            # return 받으면 같은 row에서 다른 col도 시도해야 하니까, 방금 놓았던 퀸을 “없었던 일”로 만들기
            cols[col] = diag1[row + col] = diag2[row - col + N - 1] = False
            
backtrack(0)
print(cnt)