import sys
input = sys.stdin.readline

N = int(input())
A = [int(input()) for i in range(N)]
A.sort()
for i in range(N):
    print(A[i])
    