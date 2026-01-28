import math
M,N = map(int,input().split())

# M부터 N까지의 1차원 리스트 생성
num_list = [0] * (N+1)

# 반복문에서 N번 돌리지 말고 루트N번 돌릴려면 2의 배수부터 지워야 됨
for i in range(2,N+1):
    num_list[i] = i
    
# 에라토스테네스의 체 구현
# for i in range(N): 이렇게 전체 N번 돌필요 없음
for i in range(2,int(math.sqrt(N))+1):    # N의 제곱근 까지만 돌려도 큰 수들은 다 제거됨
    if num_list[i] == 0:
        continue
    for j in range(i+i,N+1,i):
        num_list[j] = 0
        
for i in range(M,N+1):
    if num_list[i] != 0:
        print(num_list[i],end='\n')