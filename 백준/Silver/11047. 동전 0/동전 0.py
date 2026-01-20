import sys
input = sys.stdin.readline

N,K = map(int,input().split())
A = [0] * N

# 데이터 삽입
for i in range(N):
    A[i] = int(input())
    
count = 0
# 큰 동전부터 선택하면서 K원 만들기
for i in range(1,N+1):
    now_max = A[-i]
    
    if now_max <= K:
        # 몫은 동전 개수에 해당
        count += int(K // now_max)
        
        # 나머지는 나머지 금액에 해당
        K = K % now_max

print(count)