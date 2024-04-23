import sys
import math
input = sys.stdin.readline

n, m = map(int, input().split())
M = int(math.sqrt(m))
A = list(range(M + 1))

A[1] = 0

for i in range(int(math.sqrt(M)) + 1):
    if A[i] == 0:
        continue
    else:
        for j in range(i + i, M + 1, i):
            A[j] = 0

answer = 0

for i in range(len(A)):
    if A[i] != 0:
        tmp = A[i]
        while A[i] <= m/tmp:
            if A[i] >= n/tmp:
                answer += 1
            tmp = A[i] * tmp

print(answer)