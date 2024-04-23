import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    print('@'*n + " "*3*n + "@"*n)

for _ in range(n):
    print("@"*(3*n + 2*n))

for _ in range(n):
    print('@'*n + " "*3*n + "@"*n)

for _ in range(n):
    print("@"*(3*n + 2*n))
    
for _ in range(n):
    print('@'*n + " "*3*n + "@"*n)