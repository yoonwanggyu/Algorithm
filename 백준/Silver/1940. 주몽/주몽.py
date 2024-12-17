# 정렬 알고리즘 시간 복잡도 : O(nlogn)

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
numbers = list(map(int,input().split()))
numbers.sort()
count = 0
i = 0
j = n -1 

while i < j: # 투 포인터 이동 원칙 따라 포인터를 이동하며 처리
    if numbers[i] + numbers[j] < m:
        i += 1
    elif numbers[i] + numbers[j] > m:
        j -= 1
    else:
        count += 1
        i += 1
        j -= 1
print(count)
