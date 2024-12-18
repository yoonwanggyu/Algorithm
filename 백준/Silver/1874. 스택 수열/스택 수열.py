import sys
input = sys.stdin.readline

# 스택 문제 - 후입선출
N = int(input())
A = [0] * N # 수열 리스트 
for i in range(N):
    A[i] = int(input()) # ex) [4,3,6,8,7,5,2,1]
    
stack = [] # 쌓을 빈스택
num = 1 # 현재 수열 값과 비교할 자연수
result = True
answer = ""

# 문제 풀이 코드
for i in range(N):
    now_su = A[i]
    if now_su >= num: # 값이 같아질 때까지 stack에 append    
        while A[i] >= num:
            stack.append(num)
            num += 1
            answer += "+\n" 
        stack.pop() # now_su랑 num이 같으면 빼기
        answer += "-\n"
    else: # 현재 수열값이 자연수보다 작으면 빼기
        n = stack.pop()
        if n > now_su:
            print("NO")
            result = False
            break
        else:
            answer += "-\n"
if result:
    print(answer)
        
    
    