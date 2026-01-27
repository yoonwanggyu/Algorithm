# -를 기준으로 잘라서 저장
num_list = list(map(str,input().split("-")))

# +를 기준으로 숫자 더하는 함수 구현
def mySum(nums:str):
    total = 0
    temp = nums.split("+")
    for i in temp:
        total += int(i)
    return total

# 정답 구하기
answer = 0
for i in range(len(num_list)):
    # 더하기 함수로 더하거나 말거나
    temp = mySum(num_list[i])
    # 첫 번째 값은 그냥 answer에 더하기
    if i == 0:
        answer += temp
    # 그 이외에는 더하기 함수 값들을 빼주기
    else:
        answer -= temp

print(answer)