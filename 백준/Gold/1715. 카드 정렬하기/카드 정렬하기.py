from queue import PriorityQueue

N = int(input())
myque = PriorityQueue()

# 데이터 삽입
for _ in range(N):
    data = int(input())
    myque.put(data)
    # myque에 삽입된 데이터들은 전체 오름차순은 아니지만 맨 앞(0번째 인덱스)은 항상 최소
    
# 전체에서 항상 최소값 두개를 뽑고 더해서 다시 myque에 집어넣기
# 결국 마지막에는 myque 원소가 1개가 되면 끝

ans = 0

while myque.qsize() > 1:
    # 1) 최소 두개 뽑기
    data1 = myque.get()
    data2 = myque.get()
    # 3) 두개 더해서 새로운 데이터 만들고 다시 집어넣기
    new_data = data1 + data2
    ans += new_data
    myque.put(new_data)
    
print(ans)