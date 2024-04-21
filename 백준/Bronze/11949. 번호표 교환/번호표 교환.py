import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = []

for _ in range(n):
    A.append(int(input()))
    
for i in range(1, m+1):
    for j in range(n-1):
        if A[j] % i > A[j+1] % i:
            tmp = A[j]
            A[j] = A[j+1]
            A[j+1] = tmp

for i in A:
    print(i)