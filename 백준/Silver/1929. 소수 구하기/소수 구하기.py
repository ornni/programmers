import sys
import math
input = sys.stdin.readline

n, m = map(int, input().split())

A = list(range(m+1))
A[1] = 0

for i in range(2, int(math.sqrt(m))+1):
    if A[i] == 0:
        continue
    for j in range(i + i, m+1, i):
        A[j] = 0

for i in A[n:m+1]:
    if i != 0:
        print(i)