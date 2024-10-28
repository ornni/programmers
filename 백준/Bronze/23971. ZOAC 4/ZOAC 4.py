import sys
input = sys.stdin.readline

h, w, n, m = map(int, input().split())

y = (h-1) // (n+1)
x = (w-1) // (m+1)

print((y+1) * (x+1))