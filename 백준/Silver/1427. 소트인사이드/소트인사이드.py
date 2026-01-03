import sys
input = sys.stdin.readline

# 1. 문자열로 받으면서 바로 리스트로 변환
# split()은 공백을 자르는 건데, 이건 공백이 없으니 그냥 list()로 감싸면 한 글자씩 쪼개집니다.
# strip()은 줄바꿈 문자(\n)를 제거하기 위해 사용합니다.
A = list(input().strip()) 

# A는 현재 ['2', '1', '4', '3'] 상태입니다.

# 2. 내림차순 정렬
A.sort(reverse=True)

# A는 현재 ['4', '3', '2', '1'] 상태입니다.

# 3. 리스트 안의 문자들을 공백 없이 합쳐서(join) 출력
print(''.join(A))