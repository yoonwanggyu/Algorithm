import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
answer = [0] * N
stack = [] # 자릿값 들어감

for i in range(N):
    # stack이 빌 때까지 반복
    while stack and A[stack[-1]] < A[i]:
        answer[stack.pop()] = A[i]
    stack.append(i)
# 스택에 남아있는 index에 -1 저장
while stack:
    answer[stack.pop()] = -1 # answer = [5,7,7,-1]
# 출력 형태로 변환
print(' '.join(map(str, answer)))