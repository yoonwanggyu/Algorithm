import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
A.sort() # 정렬
count = 0

# 단, 정렬 데이터에서 자기 자신을 좋은 수 만들기에 포함하면 안됨!!
for k in range(N):
    find = A[k]
    i = 0
    j = N - 1 
    while i < j: # 투 포인터 알고리즘
        if A[i] + A[j] < find:
            i += 1
        elif A[i] + A[j] > find:
            j -= 1
        else: # find는 서로 다른 두 수의 합이어야 함을 체크
            if i != k and j != k:
                count += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
print(count)