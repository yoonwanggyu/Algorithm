import sys
input = sys.stdin.readline

N = int(input())

# 1) sort() 오름차순으로 풀기
# A = [int(input()) for i in range(N)]
# A.sort()
# for i in range(N):
#     print(A[i])

# 2) 버블 정렬로 풀기
A = [int(input()) for i in range(N)]    # [5,2,3,4,1]
for i in range(N-1):        # A 리스트 전체 도는 횟수
    for j in range(N-1-i):  # 한번 돌 때마다 자리 바꿈을 검사하는 횟수
        if A[j] > A[j+1]:
            temp = A[j]     
            A[j] = A[j+1]   # i번째에 i+1번째 값으로 바꾸고
            A[j+1] = temp   # i+1번째에는 i번째 값으로 바꾸기
for i in range(N):
    print(A[i])

    
