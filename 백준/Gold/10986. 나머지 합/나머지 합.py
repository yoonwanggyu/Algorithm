import sys
input = sys.stdin.readline

# 핵심 아이디어 : (A+B) % C = ((A % C) + (B % C)) % C

n,m = map(int,input().split())

A = list(map(int,input().split())) # 원본 배열
B = [0] * n # 합 배열
C = [0] * m # 같은 나머지의 인덱스를 카운트하는 리스트
B[0] = A[0]
answer = 0

for i in range(1,n):
    B[i] = B[i-1] + A[i]
    
for i in range(n):
    reminder = B[i] % m
    if reminder == 0:
        answer += 1
    C[reminder] += 1

for i in range(m):
    # 나머지가 같은 인덱스 중 2개를 뽑는 경우의 수를 더하기
    if C[i] > 1:
        answer += (C[i] * (C[i]-1) // 2)
        
print(answer)
    
