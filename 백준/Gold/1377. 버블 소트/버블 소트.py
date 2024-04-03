import sys
input = sys.stdin.readline

n = int(input())
A =[]

for i in range(n):
    A.append((int(input()), i))

A.sort()

max = 0

for i in range(n):
    if max < A[i][1] - i:
        max = A[i][1] - i

print(max + 1)