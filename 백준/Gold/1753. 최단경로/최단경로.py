import sys
input = sys.stdin.readline
from queue import PriorityQueue

V,e = map(int, input().split())
k = int(input())
distance = [sys.maxsize] * (V+1)
visited = [False] * (V+1)
A = [[] for _ in range(V+1)]
queue = PriorityQueue()

for _ in range(e):
    u, v, w = map(int, input().split())
    A[u].append((v, w))

queue.put((0, k))
distance[k] = 0

while queue.qsize() > 0:
    now = queue.get()
    c_v = now[1]
    if visited[c_v]:
        continue
    visited[c_v] = True
    for temp in A[c_v]:
        next = temp[0]
        weight = temp[1]
        if distance[next] > distance[c_v] + weight:
            distance[next] = distance[c_v] + weight
            queue.put((distance[next], next))

for i in range(1, V+1):
    if visited[i]:
        print(distance[i])
    else:
        print("INF")