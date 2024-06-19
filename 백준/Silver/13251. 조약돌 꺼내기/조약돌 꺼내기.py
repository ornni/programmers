import sys
input = sys.stdin.readline

probability = [0] * 51
m = int(input())
colors = list(map(int, input().split()))
total = 0

for i in colors:
    total += i

k = int(input())
answer = 0

for i in range(m):
    if colors[i] >= k:
        probability[i] = 1
        for j in range(k):
            probability[i] = probability[i] * (colors[i] - j) / (total - j)
        answer += probability[i]

print(answer)