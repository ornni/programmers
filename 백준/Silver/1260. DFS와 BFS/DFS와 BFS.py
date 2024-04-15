import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n, m, v = map(int, input().split())
A = [[] for _ in range(n+1)]
visited = [False] * (n+1)

def DFS(x):
    print(x, end = ' ')
    visited[x] = True
    for i in A[x]:
        if not visited[i]:
            DFS(i)

for _ in range(m):
    e, s = map(int, input().split())
    A[e].append(s)
    A[s].append(e)

for i in range(n+1):
    A[i].sort()

DFS(v)

def BFS(x):
    queue = deque()
    queue.append(x)
    visited[x] = True
    while queue:
        now = queue.popleft()
        print(now, end = ' ')
        for i in A[now]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

print()
visited = [False] * (n+1)
BFS(v)