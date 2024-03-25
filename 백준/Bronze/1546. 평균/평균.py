n = int(input())
score = list(map(int, input().split()))

m = max(score)
new_score = []

for i in range(n):
    new = score[i]/m*100
    new_score.append(new)

answer = sum(new_score)/n
print('{:.2f}'.format(answer))