import sys
input = sys.stdin.readline
N = int(input())

# 정렬이 총 몇 번 인지 = 안쪽 for 문이 몇 번 수행됐는지 구하는 문제 흐름대로 작성하기
# 1) 인덱스도 같이 저장 (값, 인덱스)
A = [(int(input()),i) for i in range(N)]
# [(10,0),(1,1),(5,2),(2,3),(3,4)]

# 2) 리스트 정렬
sorted_A = sorted(A)
# [(1, 1), (2, 3), (3, 4), (5, 2), (10, 0)]

# 3) 정렬 전 인덱스 - 정렬 후 인덱스 max 값 찾기
Max = 0
for i in range(N):
    # 정렬 전 index - 정렬 후 index 계산의 최댓값 저장
    if Max < sorted_A[i][1]-i:
        Max = sorted_A[i][1]-i
print(Max+1)