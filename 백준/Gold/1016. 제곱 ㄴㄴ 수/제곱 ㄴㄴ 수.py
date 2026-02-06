import math

Min,Max = map(int, input().split())
check_list = [False] * (Max-Min+1)

for i in range(2, int(math.sqrt(Max) + 1)):
    square_num = i * i
    
    # 만약 min값이 4보다 큰 경우 첫 시작부분을 찾기 위해 아래처럼 start_index 구현
    start_index = Min // square_num
    if Min % square_num != 0:
        start_index += 1
        
    # 이제 구한 index부터 제곱수의 배수들을 탐색하며 True로 변경하기
    for j in range(start_index, Max // square_num + 1):
        check_list[int((j*square_num)-Min)] = True

# 제곱이 아닌 수만 세면 됨(False인 애들만)
count = 0
for i in range(len(check_list)):
    if not check_list[i]:
        count += 1
print(count)