import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N = int(input())

# 1) 소수 판별 함수( √x까지만 보자)
    # 만약 √x까지의 수들을 나눴을 때 0이 나온다면 합성수 즉, 소수가 아니다
def is_prime(num):
    # 0,1은 소수가 아니다
    if num < 2:
        return False
    # 2는 소수이다.
    if num == 2:
        return True
    # 짝수는 소수가 아니다
    if num % 2 == 0:
        return False
    # 홀수의 약수만 검사하자
        # 소수가 아니면 (합성수)x = a * b 형태로 약수가 있는데, 만약 a와 b가 둘 다 √x보다 크면 a*b > √x * √x = x 가 되어버려서 모순
        # 즉, 합성수라면 약수 중 하나는 반드시 √x 이하에 있음. 그래서 d를 √x까지만 확인하면 충분.
        # d * d <= x 는 d <= √x 와 똑같은 의미
    d = 3    # 홀수 중 가장 작은 수부터 시작
    while d * d <= num:
        if num % d == 0:
            return False
        d += 2
    return True

# 2) 재귀함수로 DFS 구현
def dfs(num):
    if len(str(num)) == N:
        print(num)
        
    # 어짜피 자릿수가 증가할 때마다 붙는 수들은 홀수 / 짝수가 붙으면 소수가 안됨
    else:
        for i in range(1,10,2):
            # 자릿수 증가시키면서 홀수 붙이기 / num = 2이라면 21/23/25/27/29들을 소수인지 판별 진행
            if is_prime(num*10 + i):
                # True(소수라면) 재귀적으로 돌기
                dfs(num*10 + i)

# 초기값인 소수인 일의 자리 수는 2,3,5,7이므로 이 수부터 시작
dfs(2)
dfs(3)
dfs(5)
dfs(7)