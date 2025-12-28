# 투 포인터

n = int(input())

# 초기값 설정
count = 1
start_index = 1
end_index = 1
sum = 1

# 경우의 수에 맞게 투 포인터를 움직이며 찾기
# 1) sum = n
# 2) sum > n
# 3) sum < n

while end_index != n:
    if sum == n:
        count += 1
        end_index += 1
        sum += end_index
    elif sum > n:
        sum -= start_index
        start_index += 1
    else:
        end_index += 1
        sum += end_index
print(count)