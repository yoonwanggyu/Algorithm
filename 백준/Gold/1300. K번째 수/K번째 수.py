N = int(input())
K = int(input())

start = 1
end = K
ans = 0

# 배열이 나오지만 배열을 만들지 않고 이진 탐색으로 푸는 문제
# 배열을 만들고 정렬하게 되면 시간 초과

# 이진탐색
while start <= end:
    middle = int((start + end) / 2)
    cnt = 0
    
    # 중앙값보다 작은 수의 개수 세기
    # 행렬 자체를 안만들었으니, 개수를 세는 공식으로 풀자
    # 각 행에서 min(N, x/i)하면 x보다 작은 수의 개수 셀 수 있음
    for i in range(1,N+1):
        cnt += min(N, int((middle / i)))
        
    # 중앙값보다 작은 수의 개수가 K 보다 작으면 중앙 + 1
    # 중앙값보다 큰 수의 개수가 K 보다 크면 중앙 - 1
    if cnt < K:
        start = middle + 1
    else:
        ans = middle
        end = middle - 1
        
print(ans)
