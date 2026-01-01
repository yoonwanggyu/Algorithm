import sys
input = sys.stdin.readline

N = int(input())
A = []
for i in range(N):
    A.append(int(input()))
    
stack = []    # 비교하면 쌓을 스택
num = 1
answer = []
result = True    # No 부분에서 break를 걸어도 마지막에 print가 찍히기 때문에 result가 True인 경우만 마지막 print 찍히게

# 현재 값이랑 수열 값이랑 비교하면서 넣엏다 뺏다 진행
# 현재 값이 수열보다 클 경우 작을 경우 나눠서 생각
for i in range(N):
    now_su = A[i]
    
    if now_su >= num:         # 값이 같아질 때까지 stack에 append  
        while now_su >= num:
            stack.append(num)
            num += 1
            answer.append('+')
        stack.pop()           # 값이 같아지면 pop 빼기
        answer.append('-')
        
    else:                     # 현재 수열값이 자연수보다 작으면 빼기
        if not stack:          # 스택 비었는지 체크
            print("NO")
            result = False
            break
        n = stack.pop()
        if n != now_su:        # 반드시 같아야 함
            print("NO")
            result = False
            break
        answer.append('-')
            
if result:
    for i in answer:
        print(i)