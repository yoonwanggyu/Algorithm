n = input()
score = list(map(int,input().split()))
max_score = max(score)
sum_score = sum(score)

print(sum_score * 100 / max_score / int(n))