import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
A = []
distance = [sys.maxsize] * (n+1)

for i in range(m):
    s, e, t = map(int, input().split())
    A.append((s, e, t))

distance[1] = 0

for _ in range(n-1):
    for s, e, t in A:
        if distance[s] != sys.maxsize and distance[e] > distance[s] + t:
            distance[e] = distance[s] + t

cycle = False

for s, e, t in A:
    if distance[s] != sys.maxsize and distance[e] > distance[s] + t:
           cycle = True

if not cycle:
     for i in range(2, n+1):
        if distance[i] != sys.maxsize:
            print(distance[i])
        else:
            print(-1)
else:
    print(-1)