import sys
input = sys.stdin.readline

n, k = map(int, input().split())
A = []
answer = 0

for _ in range(n):
    A.append(int(input()))

A.sort(reverse = True)

for i in A:
    if i <= k:
        answer += k // i
        k = k % i

print(answer)