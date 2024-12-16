# 구간 합 개념 적용 문제
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
numbers = list(map(int,input().split())) # 5 4 3 2 1
prefix_sum = [0]                         # 0 5 9 12 14 15
temp = 0

# 합 배열 만들기 -> S[i] = S[i-1] + A[i]
for i in numbers:
    temp += i
    prefix_sum.append(temp)
    
# 구간 합 구하기
for i in range(m):
    a,b = map(int,input().split())
    print(prefix_sum[b] - prefix_sum[a-1])