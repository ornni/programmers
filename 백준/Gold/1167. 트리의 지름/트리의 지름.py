import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
A = [[] for _ in range(n+1)]

for _ in range(n):
    data = list(map(int, input().split()))
    index = 0
    s = data[index]
    index += 1
    while True:
        e = data[index]
        if e == -1:
            break
        v = data[index + 1]
        A[s].append((e, v))
        index += 2
        
distance = [0] * (n+1)
visited = [False] * (n+1)

def BFS(x):
    queue = deque()
    queue.append(x)
    visited[x] = True
    
    while queue:
        now = queue.popleft()
        for i in A[now]:
            if not visited[i[0]]:
                visited[i[0]] = True
                queue.append(i[0])
                distance[i[0]] = distance[now] + i[1]

BFS(1)
Max = 1

for i in range(2, n+1):
    if distance[Max] < distance[i]:
        Max = i

distance = [0] * (n+1)
visited = [False] * (n+1)
BFS(Max)
print(max(distance))