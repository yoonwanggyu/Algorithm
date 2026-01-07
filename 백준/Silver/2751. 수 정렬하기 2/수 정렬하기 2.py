import sys
input = sys.stdin.readline
print = sys.stdout.write

# 병합 정렬로 풀기!!
    # 로직 : 분할 -> 정렬 -> 병합
def merge_sort(arr:list, temp:list, start_idx, end_idx):
    # 원소가 0개 또는 1개인 구간은 이미 정렬된 상태
    if end_idx - start_idx <= 1:
        return
    
    # 1) 분할하기
    mid_idx = start_idx + (end_idx - start_idx) // 2
        # 재귀적으로 왼쪽/오른쪽을 먼저 정렬
    merge_sort(arr,temp,start_idx,mid_idx)
    merge_sort(arr,temp,mid_idx,end_idx)
    
    # 2) 병합 (Merge)
        # 이제 arr[start:mid] 와 arr[mid:end] 는 각각 '정렬된 상태'이므로,
        # 두 정렬된 구간을 작은 값부터 하나씩 뽑아 tmp[start:end]에 채운다
    i = start_idx
    j = mid_idx
    
    k = start_idx # temp list에 넣을 위치
    
        # 2-1) 양쪽 구간 모두 아직 남은 원소가 있을 때까지 비교하며 병합
    while i < mid_idx and j < end_idx:
            # 왼쪽 값이 더 작거나 같으면 왼쪽 값을 tmp에 넣고 i를 이동
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
            # 오른쪽 값이 더 작으면 오른쪽 값을 tmp에 넣고 j를 이동
        else:
            temp[k] = arr[j]
            j += 1
        k += 1
        
        # 2-2) 왼쪽 구간에 원소가 남아있다면 그대로 tmp에 복사
    while i < mid_idx:
        temp[k] = arr[i]
        i += 1
        k += 1
        
        # 2-3) 오른쪽 구간에 원소가 남아있다면 그대로 tmp에 복사
    while j < end_idx:
        temp[k] = arr[j]
        j += 1
        k += 1
        
    # 3) tmp 결과를 원본 arr로 반영 (Copy back)
        # tmp[start:end] 에는 정렬된 결과가 들어있고,
        # 이를 arr[start:end]에 덮어씌워서 실제 배열을 정렬된 상태로 만든다
    arr[start_idx : end_idx] = temp[start_idx : end_idx]
    
N = int(input())
arr = [int(input()) for _ in range(N)]
temp = [0] * N

merge_sort(arr,temp,0,N)

print("\n".join(map(str,arr)))