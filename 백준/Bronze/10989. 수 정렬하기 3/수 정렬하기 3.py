import sys
input = sys.stdin.readline
print = sys.stdout.write

# 계수 정렬로 풀어보자!
    # 1) 값들을 입력받으면 해당 값을 인덱스로 사용하고 개수를 입력
    # 2) 출력은 개수만큼 해당 값을 출력
N = int(input())
count = [0] * 10001

    # 1)
for _ in range(N):
    count[int(input())] += 1
    
    # 2)
for i in range(len(count)):
    if count[i] != 0:
        for _ in range(count[i]):
            print((str(i) + '\n'))