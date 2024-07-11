import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
tree = [[] for _ in range(n)]
visited = [False] * n
parent = list(map(int, input().split()))

for i in range(n):
    if parent[i] != -1:
        tree[i].append(parent[i])
        tree[parent[i]].append(i)
    else:
        root = i

delete_num = int(input())
answer = 0

def dfs(x):
    global answer
    visited[x] = True
    leaf = 0
    for i in tree[x]:
        if visited[i] == False and i != delete_num:
            leaf += 1
            dfs(i)
    if leaf == 0:
        answer += 1

if delete_num == root:
    print(0)
else:
    dfs(root)
    print(answer)