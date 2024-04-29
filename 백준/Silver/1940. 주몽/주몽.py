import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
A = list(map(int, input().split()))
index1 = 0
index2 = n - 1
total = 0
answer = 0
A.sort()

while index1 < index2:
    total = A[index1] + A[index2]
    if total == m:
        answer += 1
        index1 += 1
    elif total < m:
        index1 += 1
    else:
        index2 -= 1

print(answer)