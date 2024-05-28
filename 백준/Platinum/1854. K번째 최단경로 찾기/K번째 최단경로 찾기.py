import sys
import heapq
input = sys.stdin.readline

n, m, k = map(int, input().split())
distance = [[sys.maxsize] * k for _ in range(n+1)]
A = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    A[a].append((b, c))

queue = [(0, 1)]
distance[1][0] = 0

while queue:
    cost, node = heapq.heappop(queue)
    for nNode, nCost in A[node]:
        sCost = cost + nCost
        if distance[nNode][k-1] > sCost:
            distance[nNode][k-1] = sCost
            distance[nNode].sort()
            heapq.heappush(queue, [sCost, nNode])

for i in range(1, n+1):
    if distance[i][k-1] == sys.maxsize:
        print(-1)

    else:
        print(distance[i][k-1])