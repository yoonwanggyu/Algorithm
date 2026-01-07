import sys
input = sys.stdin.readline

# 병합 정렬로 버블 정렬의 swap 횟수 구할 수 있음
# => 병합 과정에서 오른쪽 원소가 왼쪽 원소를 뛰어넘는 경우를 이용해 교차 inversion을 계산함    

def merge_sort(arr:list,temp:list, start_idx,end_idx):
    # 1) 원소의 개수가 0또는 1인 경우는 정렬 끝난 상태
    if end_idx - start_idx <= 1:
        return 0
    
    # 2) mid값 정해서 분할
    mid_idx = start_idx + (end_idx - start_idx) // 2
    
    # 3) 재귀적으로 왼쪽/오른쪽 분할하면서 정렬하고 inv 반환하니까 inv에 더해주기
    inv = 0
    inv += merge_sort(arr,temp,start_idx,mid_idx)    # 왼쪽에서 나온 swap 횟수
    inv += merge_sort(arr,temp,mid_idx,end_idx)      # 오른쪽에서 나온 swap 횟수
    
    # 4) 병합
    i = start_idx
    j = mid_idx
    k = start_idx
    
    while i < mid_idx and j < end_idx:
        if arr[i] <= arr[j]:    # 왼쪽이 더 작을 경우는 swap이 일어나지 않고 바로 temp에 들어감
            temp[k] = arr[i]
            i += 1
        else:       # 오른쪽이 더 작을 경우는 swap이 일어남 -> ex) [3,1]에서 1이 더 작으므로 자리 바뀜 [1,3]
            temp[k] = arr[j]
            j += 1
            # 이때 swap이 일어나는 횟수는 이전 데이터의 개수 -> ex) [3,2,1]에서 1이 맨 앞으로 가려면 
            # [3,1,2]가 된 다음에 [1,3,2]가 됨. 즉 1앞에 있던 데이터 개수 2개가 swap이 일어난 횟수가 됨
            # 왼쪽에 남아있는 i..mid-1 모두가 arr[j]보다 큼 → 그 개수만큼 inversion 증가
            inv += (mid_idx - i)
        k += 1
        
    # 5) 남은 원소 복사   
    while i < mid_idx:
        temp[k] = arr[i]
        i += 1
        k += 1
    while j < end_idx:
        temp[k] = arr[j]
        j += 1
        k += 1
        
    # 6) 병합 결과를 원본 배열에 반영
    arr[start_idx:end_idx] = temp[start_idx:end_idx]
    
    return int(inv)
        
N = int(input())
arr = list(map(int,input().split()))
temp = [0] * N

print(merge_sort(arr,temp,0,N))