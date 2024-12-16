# <2차원 구갑 합 배열을 어떻게 구성할지 고민하는 것이 문제>

# 아래 순서대로 문제 풀기

# 1) 2차원 구간 합 배열의 1행, 1열부터 구하기
     # D[1][j] = D[1][j-1] + A[1][j]
     # D[j][1] = D[j-1][1] + A[j][1]
# 2) 나머지 2차원 구간 합 배열 채우기
     # D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]
# 3) 문제에 주어진 구간 합 계산하기
     # ex) 전체(마지막 구간 합) - 1행 - 1열 + (1,1)
     # D[X2][Y2] - D[X1-1][Y2] - D[X2][Y1-1] + DD[X1-1][Y1-1]
        
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
A = [[0] * (n+1)] # 원본 배열
D = [[0] * (n+1) for _ in range(n+1)] # 구간 합 배열

# 원본 배열에 넣기
for i in range(n):
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)
    
# 구간 합 배열 넣기
for i in range(1,n+1):
    for j in range(1,n+1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]
        
# 문제 풀기
for _ in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(result)
