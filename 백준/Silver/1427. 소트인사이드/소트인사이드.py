import sys
input = sys.stdin.readline

A = list(input())

n = len(A)
for i in range(n):
    for j in range(n-i-1):
        if A[j] > A[j+1]:
            temp = A[j]
            A[j] = A[j+1]
            A[j+1] = temp
A.reverse()

print(''.join(A))