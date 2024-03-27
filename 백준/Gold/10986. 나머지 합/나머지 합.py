import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))
S = [0]*n
C = [0]*m
count = 0

S[0] = A[0]
for i in range(1, n):
    S[i] = S[i-1] + A[i]

for i in range(n):
    sm = S[i] % m
    if sm == 0:
        count += 1
    C[sm] += 1

for i in range(m):
    if C[i]>1:
        count += (C[i] * (C[i]-1) // 2)

print(count)
