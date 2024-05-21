import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
iseven = True

def DFS(x):
    global iseven
    visited[x] = True
    for i in A[x]:
        if not visited[i]:
            check[i] = (check[x] + 1) % 2
            DFS(i)
        elif check[x] == check[i]:
            iseven = False

for _ in range(n):
    v, e = map(int, input().split())
    A = [[] for _ in range(v+1)]
    visited = [False] * (v+1)
    check = [0] * (v+1)
    iseven = True

    for i in range(e):
        start, end = map(int, input().split())
        A[start].append(end)
        A[end].append(start)
    
    for i in range(1, v+1):
        if iseven:
            DFS(i)
        else:
            break
    
    if iseven:
        print("YES")
    else:
        print("NO")