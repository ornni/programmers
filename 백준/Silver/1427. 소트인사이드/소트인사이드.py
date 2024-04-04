import sys
input = sys.stdin.readline

A = list(input())
A = A[:-1]
n = len(A)
for i in range(n):
    for j in range(n-1, i, -1):
        if A[j] > A[j-1]:
            temp = A[j]
            A[j] = A[j-1]
            A[j-1] = temp

print(''.join(A))