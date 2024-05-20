import sys
input = sys.stdin.readline
from collections import deque

n, m, k, x = map(int, input().split())
A = [[] for _ in range(n+1)]
answer = []
visited = [-1] * (n+1)

for _ in range(m):
    s, e = map(int, input().split())
    A[s].append(e)

def BFS(x):
    queue = deque()
    queue.append(x)
    visited[x] += 1

    while queue:
        now = queue.popleft()
        for i in A[now]:
            if visited[i] == -1:
                visited[i] = visited[now] + 1
                queue.append(i)

BFS(x)

for i in range(n+1):
    if visited[i] == k:
        answer.append(i)

if not answer:
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)