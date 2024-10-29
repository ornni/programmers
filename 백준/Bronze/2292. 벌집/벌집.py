n = int(input())

total = 1
answer = 0

while total < n:
    answer += 1
    total += (6 * answer)

print(answer + 1)