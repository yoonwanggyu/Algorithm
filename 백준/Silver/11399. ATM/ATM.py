import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))

# 삽입 정렬 구현
for i in range(1,N):
    # 정렬 대상 값
    insert_idx = i
    insert_value = A[i]
    
    # 정렬 대상 값 이전 범위에서 값들을 훓고 정렬시킬 위치에 삽입
    # 뒤에서부터 하나씩 비교
    for j in range(i-1,-1,-1):    # 0포함
        # 현재값이 이전 값보다 크면 현재 값을 삽입할 idx는 이전 값 바로 오른쪽
        if A[j] < A[i]:
            insert_idx = j+1
            break
        if j == 0:
            insert_idx = 0
    
    # 값들을 하나씩 밀기
    for k in range(i,insert_idx,-1):
        A[k] = A[k-1]
    
    # 오른쪽으로 밀고 빈 곳에 값 넣기
    A[insert_idx] = insert_value
    
# 합 배열 만들고 출력
# S[i] = S[i-1] + A[i]
S = [0] * N
S[0] = A[0]
for i in range(1,N):
    S[i] = S[i-1] + A[i]
    
# 답 출력
sum = 0
for i in range(N):
    sum += S[i]
print(sum)