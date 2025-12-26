import sys
input = sys.stdin.readline

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, diff):
        while i <= self.n:
            self.bit[i] += diff
            i += i & -i

    def prefix_sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def range_sum(self, l, r):
        return self.prefix_sum(r) - self.prefix_sum(l - 1)

N, M, K = map(int, input().split())

arr = [0] * (N + 1)
fw = Fenwick(N)

# N줄 입력
for i in range(1, N + 1):
    x = int(input())
    arr[i] = x
    fw.add(i, x)

# M+K 쿼리 처리
for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        # b번째 값을 c로 변경
        diff = c - arr[b]
        arr[b] = c
        fw.add(b, diff)
    else:
        # b~c 구간합
        print(fw.range_sum(b, c))