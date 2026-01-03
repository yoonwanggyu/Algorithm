import sys
input = sys.stdin.readline
print = sys.stdout.write

# 1) sort(reverse=True)로 풀기
    # 1. 문자열로 받으면서 바로 리스트로 변환
    # split()은 공백을 자르는 건데, 이건 공백이 없으니 그냥 list()로 감싸면 한 글자씩 쪼개집니다.
    # strip()은 줄바꿈 문자(\n)를 제거하기 위해 사용합니다.
# A = list(input().strip()) # ['2', '1', '4', '3']

    # 2. 내림차순 정렬
# A.sort(reverse=True) # ['4', '3', '2', '1']

    # 3. 리스트 안의 문자들을 공백 없이 합쳐서(join) 출력
# print(''.join(A))

# 2) 선택 정렬로 풀기 = 내림차순이므로 최댓값을 찾아 기준이 되는 자리와 swap
A = list(input())

for i in range(len(A)):
    # 기준값 설정 / 현재 자리가 가장 크다고 가정
    Max_idx = i

    # max값 찾기
    for j in range(i+1,len(A)):
        if A[j] > A[Max_idx]:
            Max_idx = j        # 진짜 max값의 인덱스(자리) 기억
            
    # 기준값보다 진짜 max가 크면 위치 바꾸기 (기준값과 진짜 max값이 같을 수도 있기 때문)
    if A[i] < A[Max_idx]:
        temp = A[i]
        A[i] = A[Max_idx]
        A[Max_idx] = temp

for i in range(len(A)):
    print(A[i])
