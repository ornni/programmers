import sys
input = sys.stdin.readline
from queue import PriorityQueue

n = int(input())
m = int(input())
distance = [sys.maxsize] * (n+1)
visited = [False] * (n+1)
A = [[] for _ in range(n+1)]

for _ in range(m):
    s, e, w = map(int, input().split())
    A[s].append((e, w))

start, end = map(int, input().split())

def dijstra(start, end):
    queue = PriorityQueue()
    queue.put((0, start))
    distance[start] = 0

    while queue.qsize() > 0:
        nowNode = queue.get()
        now = nowNode[1]

        if not visited[now]:
            visited[now] = True
            for n in A[now]:
                if not visited[n[0]] and distance[n[0]] > distance[now] + n[1]:
                    distance[n[0]] = distance[now] + n[1]
                    queue.put((distance[n[0]], n[0]))
    return distance[end]

print(dijstra(start, end))