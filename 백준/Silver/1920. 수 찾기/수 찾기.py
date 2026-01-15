import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
M = int(input())
target_nums = list(map(int,input().split()))

# 이진 탐색을 위한 정렬
A.sort()

for i in range(M):
    target_num = target_nums[i]
    find = False
    
    # 이진 탐색 시작
    start_idx = 0
    end_idx = len(A)-1
    while start_idx <= end_idx:
        # 중앙값 찾고
        mid_idx = int((start_idx + end_idx) / 2)
        mid = A[mid_idx]
        
        # 중앙값과 타깃값 계속 비교하면서 범위 줄이기
        if mid < target_num:
            start_idx = mid_idx + 1
        elif mid > target_num:
            end_idx = mid_idx - 1
        else:
            find = True
            break
            
    if find:
        print(1)
    else:
        print(0)