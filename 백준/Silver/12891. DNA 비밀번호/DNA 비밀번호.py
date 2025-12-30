import sys 
input = sys.stdin.readline

S,P = map(int,input().split())
DNA = input().strip()
checklist = list(map(int, input().split()))

idx = {'A':0,'C':1,'G':2,'T':3}
mylist = [0,0,0,0]
result = 0

# 초기 슬라이딩 설정(시작값)
for i in DNA[:P]:
    mylist[idx[i]] += 1
if mylist[0] >= checklist[0] and mylist[1] >= checklist[1] and mylist[2] >= checklist[2] and mylist[3] >= checklist[3]:
    result += 1
    
# 슬라이딩
for i in range(P,S):
    l = i - P
    # 새로 들어오는 문자
    mylist[idx[DNA[i]]] += 1
    # 윈도우가 오르쪽으로 한칸 이동하면서 이전에 있던 빠지는 문자
    mylist[idx[DNA[l]]] -= 1
    
    if mylist[0] >= checklist[0] and mylist[1] >= checklist[1] and mylist[2] >= checklist[2] and mylist[3] >= checklist[3]:
        result += 1
        
print(result)