import sys
input = sys.stdin.readline

n = int(input())

a0 = 0
a1 = 1

if n == 1:
    print(a1)
else:
    for _ in range(n-1):
        a2 = a0 + a1
        a0 = a1
        a1 = a2
    print(a2)