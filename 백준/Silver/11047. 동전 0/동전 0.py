n, k = map(int, input().split())
A = []
count = 0

for _ in range(n):
    A.append(int(input()))

for i in range(n-1, -1, -1):
    if A[i] <= k:
        count += (k // A[i])
        k = (k % A[i])

print(count)