import sys
input = sys.stdin.readline

# 내 맨 처음 구현 코드 -> 시간 초과 : 시간 복잡도 O(N) 초과 -> 슬라이딩 윈도우가 아님 

# S , P = map(int,input().split())
# DNA = list(input())
# A,C,G,T = map(int,input().split())
# answer = 0
# i = 0
# j = P
# check_list = 0

# 반복 횟수: N번
# 각 반복 시 count 연산: 최악의 경우 최대 4회
# 각 count 연산 복잡도: O(P)
# 최종 시간 복잡도는 O(N * P) 가 됩니다.

# for _ in range(S):
#     password = DNA[i:j]
#     if password.count("A") >= A:
#        check_list += 1
#     elif password.count("C") >= C:
#         check_list += 1
#     elif password.count("G") >= G:
#         check_list += 1
#     elif password.count("T") >= T:
#         check_list += 1
    
#     if check_list == 4:
#         answer += 1
# print(answer)

# 슬라이딩 윈도우 방식으로 하자
# 현재 상태 리스트를 업데이트 할 때는 빠지는 문자열, 신규 문자열만 보고 업데이트 하는 방식으로 진행하자
# 기존 검사 결과에 새로 들어온 문자열, 제거되는 문자열만 반영하여 확인하는 것이 핵심

import sys
input = sys.stdin.readline

# 전역 변수 선언
checklist = [0] * 4
mylist = [0] * 4
checksecret = 0

# 문자 더하기 함수 선언
def myadd(c):
    global checklist, mylist, checksecret
    if c == "A":
        mylist[0] += 1
        if mylist[0] == checklist[0]:
            checksecret += 1
    elif c == "C":
        mylist[1] += 1
        if mylist[1] == checklist[1]:
            checksecret += 1
    elif c == "G":
        mylist[2] += 1
        if mylist[2] == checklist[2]:
            checksecret += 1
    elif c == "T":
        mylist[3] += 1
        if mylist[3] == checklist[3]:
            checksecret += 1

# 문자 빼기 함수 선언
def myremove(c):
    global checklist,mylist,checksecret
    if c == "A":
        if mylist[0] == checklist[0]:
            checksecret -= 1
        mylist[0] -= 1
    elif c == "C":
        if mylist[1] == checklist[1]:
            checksecret -= 1
        mylist[1] -= 1
    elif c == "G":
        if mylist[2] == checklist[2]:
            checksecret -= 1
        mylist[2] -= 1
    elif c == "T":
        if mylist[3] == checklist[3]:
            checksecret -= 1
        mylist[3] -= 1

# 메인 코드
S, P = map(int,input().split())
DNA = list(input().strip())
checklist = list(map(int,input().split()))
result = 0

# checklist가 0인 부분은 이미 조건 만족이므로 checksecret += 1
for i in range(4):
    if checklist[i] == 0:
        checksecret += 1

# 초기 P 부분 문자열 처리 
for i in range(P):
    myadd(DNA[i])
# 초기 윈도우 검사
if checksecret == 4:
    result += 1

# 슬라이딩
for i in range(P, S):
    j = i - P
    myadd(DNA[i])
    myremove(DNA[j])
    if checksecret == 4:
        result += 1

print(result)
