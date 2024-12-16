# 투 포인터

n = int(input())

# 초기값 설정
count = 1
start_index = 1
end_index = 1
sum = 1

# 경우의 수에 맞게 투 포인터를 움직이며 찾기
# 1) sum = n : 하나의 경우를 찾은 뒤, 구간을 확장
# 2) sum > n : 구간을 줄여 합을 작게 만들자
# 3) sum < n : 구간을 넓혀 합을 키우자

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
