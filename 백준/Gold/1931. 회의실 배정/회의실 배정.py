import sys
input = sys.stdin.readline

N = int(input())
time_list = [[0]*2 for _ in range(N)]

# 데이터 삽입 : 끝나는 시간을 기준으로 정렬하고 같다면 시작 시간을 기준으로 정렬
# 정렬을 위해 끝나는 시간을 0번째에 삽입
for i in range(N):
    s,e = map(int,input().split())
    time_list[i][1] = s
    time_list[i][0] = e
    
# 정렬 : 그냥 sort를 하게 되면 자동으로 0번째 기준으로 정렬하고 같다고 1번째 기준으로 정렬해줌
time_list.sort()

count = 0
end_time = 0
for i in range(N):
    # 이전 회의와 겹치지 않게 이전 회의의 끝나는 시간과 같거나 클경우
    if time_list[i][1] >= end_time:
        count += 1
        # 끝나는 시간 업데이트
        end_time = time_list[i][0]
    
print(count)