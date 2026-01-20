import sys
input = sys.stdin.readline

N = int(input())

# 4가지 케이스별로 나누기
pos = []
neg = []
cnt_one = 0
cnt_zero = 0
for _ in range(N):
    num = int(input())
    if num > 1:
        pos.append(num)
    elif num < 0:
        neg.append(num)
    elif num == 1:
        cnt_one += 1
    elif num == 0:
        cnt_zero += 1
        
total = 0
# 양수 처리
pos.sort(reverse=True)
i = 0
while i < len(pos) - 1:
    total += (pos[i] * pos[i+1])
    i += 2
if i == len(pos) - 1:    # 홀수개면 마지막 남은 하나는 그냥 더하기
    total += pos[-1]
    
# 음수 처리
neg.sort()
j = 0
while j < len(neg) - 1:
    total += (neg[j] * neg[j+1])
    j += 2
if j == len(neg) - 1:
    if cnt_zero > 0:
        pass                      # 0이 남으면 0이랑 곱해서 없애고
    else:
        total += neg[-1]          # 0이 없으면 그냥 음수 더하기
        
# 마무리로 1의 개수만큼 더해주기
total += cnt_one

print(total)