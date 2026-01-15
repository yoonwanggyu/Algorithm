import sys
input = sys.stdin.readline

N, M = map(int,input().split())
A = list(map(int,input().split()))

# 시작 인덱스, 종료 인덱스 구하기
start = 0
end = 0
for i in A:
    if start < i:
        start = i
    end += i
    
# 이진 탐색으로 용량 최소 구하기
while start <= end:
    count = 0    # 블루레이 개수
    mid = int((start+end) / 2)
    sum = 0      # 블루레이 크기 
    
    # 블루레이 크기랑 중간값 비교하면서 블루레이 개수 세기
    for i in range(N):
        if sum + A[i] > mid:
            count += 1
            sum = 0
        sum += A[i]
        
    # 나머지 부분이 남아 있을 경우
    if sum != 0:
        count += 1
        
    if count <= M:
        end = mid -1
    else:
        start = mid + 1
        
print(start)