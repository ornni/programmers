import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
visited = [False] * n
tree = [[] for _ in range(n)]
answer = 0
p = list(map(int, input().split()))
deleteNode = int(input())

for i in range(n):
    if p[i] != -1:
        tree[i].append(p[i])
        tree[p[i]].append(i)
    else:
        root = i

def DFS(number):
    global answer
    visited[number] = True
    cNode = 0
    for i in tree[number]:
        if not visited[i] and i != deleteNode:
            cNode += 1
            DFS(i)
    if cNode == 0:
        answer += 1

if deleteNode == root:
    print(0)
else:
    DFS(root)
    print(answer)