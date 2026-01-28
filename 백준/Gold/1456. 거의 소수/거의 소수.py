import math
A,B = map(int,input().split())

# 문제의 최대 범위에서 소수 구하기
num_list = [0] * (10000001)
for i in range(2,len(num_list)):
    num_list[i] = i
for i in range(2,int(math.sqrt(len(num_list))+1)):
    if num_list[i] == 0:
        continue
    for j in range(i+i,len(num_list),i):
        num_list[j] = 0
        
# 소수의 N 제곱수 개수 구하기
count = 0
for i in range(2,10000001):
    if num_list[i] != 0:
        p = num_list[i]
        temp = p * p
        while temp <= B:
            if temp >= A:
                count += 1
            temp *= p
print(count)