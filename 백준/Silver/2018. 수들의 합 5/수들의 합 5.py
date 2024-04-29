import sys
input = sys.stdin.readline

n = int(input())
index1 = 1
index2 = 1
total = 1
answer = 0

while index2 != n:
    if total == n:
        answer += 1
        index2 += 1
        total += index2
    elif total < n:
        index2 += 1
        total += index2
    else:
        total -= index1
        index1 += 1

print(answer + 1)