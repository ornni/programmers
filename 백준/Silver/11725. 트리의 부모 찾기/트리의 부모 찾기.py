import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
tree = [[] for _ in range(n+1)]
visited = [False] * (n+1)
answer = [0] * (n+1)

for _ in range(n-1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

def dfs(x):
    visited[x] = True
    for y in tree[x]:
        if visited[y] == False:
            answer[y] = x
            dfs(y)

dfs(1)

for i in range(2, n+1):
    print(answer[i])