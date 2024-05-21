import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
tree = [[] for _ in range(n+1)]
visited = [False] * (n+1)
answer = [0] * (n+1)

for _ in range(1, n):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

def DFS(x):
    visited[x] = True
    for i in tree[x]:
        if not visited[i]:
            answer[i] = x
            DFS(i)

DFS(1)

for i in range(2, n+1):
    print(answer[i])